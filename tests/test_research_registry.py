from tools.research_registry import Experiment, ResearchRegistry, environment_fingerprint


def sample(name="baseline", **kwargs):
    data = dict(
        name=name,
        hypothesis="smaller prompts reduce latency",
        inputs={"prompt_tokens": 100},
        environment={"python": "3.13", "platform": "linux"},
        metrics={"latency_ms": 120.0, "quality": 0.9},
        artifacts=("results.json",),
    )
    data.update(kwargs)
    return Experiment(**data)


def test_ids_are_deterministic():
    assert sample().experiment_id == sample().experiment_id


def test_duplicate_rejected():
    registry = ResearchRegistry()
    registry.add(sample())
    try:
        registry.add(sample())
    except ValueError as exc:
        assert "duplicate" in str(exc)
    else:
        raise AssertionError("duplicate experiment accepted")


def test_parent_lineage():
    registry = ResearchRegistry()
    root = sample()
    root_id = registry.add(root)
    child = sample("variant", parent_id=root_id, inputs={"prompt_tokens": 80})
    child_id = registry.add(child)
    assert [x.experiment_id for x in registry.lineage(child_id)] == [root_id, child_id]


def test_missing_parent_rejected():
    registry = ResearchRegistry()
    try:
        registry.add(sample(parent_id="missing"))
    except ValueError as exc:
        assert "parent" in str(exc)
    else:
        raise AssertionError("missing parent accepted")


def test_reproduction_provenance():
    registry = ResearchRegistry()
    original = sample()
    original_id = registry.add(original)
    replica = sample(
        "replica",
        reproduced_from=original_id,
        environment={"python": "3.13", "platform": "android"},
    )
    replica_id = registry.add(replica)
    assert [x.experiment_id for x in registry.reproductions(original_id)] == [replica_id]


def test_metric_comparison():
    registry = ResearchRegistry()
    left_id = registry.add(sample())
    right_id = registry.add(sample("variant", metrics={"latency_ms": 90.0, "quality": 0.92}))
    comparison = registry.compare_metrics(left_id, right_id)
    assert comparison["latency_ms"]["delta"] == -30.0
    assert round(comparison["quality"]["delta"], 2) == 0.02


def test_manifest_is_stable():
    a = ResearchRegistry()
    b = ResearchRegistry()
    first = sample("a")
    second = sample("b", inputs={"prompt_tokens": 50})
    for registry in (a, b):
        registry.add(second)
        registry.add(first)
    assert a.manifest() == b.manifest()


def test_environment_fingerprint_order_independent():
    left = environment_fingerprint({"python": "3.13", "os": "linux"})
    right = environment_fingerprint({"os": "linux", "python": "3.13"})
    assert left == right
