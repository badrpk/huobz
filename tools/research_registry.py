from __future__ import annotations

from dataclasses import dataclass, field, asdict
from hashlib import sha256
import json
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _digest(value: Any) -> str:
    return sha256(_canonical(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Experiment:
    name: str
    hypothesis: str
    inputs: Mapping[str, Any]
    environment: Mapping[str, str]
    metrics: Mapping[str, float]
    artifacts: Tuple[str, ...] = ()
    parent_id: Optional[str] = None
    reproduced_from: Optional[str] = None
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("experiment name is required")
        if not self.hypothesis.strip():
            raise ValueError("hypothesis is required")
        for key, value in self.metrics.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"metric {key!r} must be numeric")

    @property
    def experiment_id(self) -> str:
        payload = {
            "name": self.name,
            "hypothesis": self.hypothesis,
            "inputs": dict(self.inputs),
            "environment": dict(self.environment),
            "metrics": dict(self.metrics),
            "artifacts": list(self.artifacts),
            "parent_id": self.parent_id,
            "reproduced_from": self.reproduced_from,
        }
        return _digest(payload)[:20]

    def evidence_hash(self) -> str:
        payload = asdict(self)
        payload["experiment_id"] = self.experiment_id
        return _digest(payload)


@dataclass
class ResearchRegistry:
    _experiments: Dict[str, Experiment] = field(default_factory=dict)

    def add(self, experiment: Experiment) -> str:
        experiment_id = experiment.experiment_id
        if experiment_id in self._experiments:
            raise ValueError(f"duplicate experiment: {experiment_id}")
        if experiment.parent_id and experiment.parent_id not in self._experiments:
            raise ValueError("parent experiment is not registered")
        if experiment.reproduced_from and experiment.reproduced_from not in self._experiments:
            raise ValueError("reproduction source is not registered")
        self._experiments[experiment_id] = experiment
        return experiment_id

    def get(self, experiment_id: str) -> Experiment:
        try:
            return self._experiments[experiment_id]
        except KeyError as exc:
            raise KeyError(f"unknown experiment: {experiment_id}") from exc

    def list(self) -> List[Experiment]:
        return sorted(self._experiments.values(), key=lambda item: (item.name.lower(), item.experiment_id))

    def lineage(self, experiment_id: str) -> List[Experiment]:
        chain: List[Experiment] = []
        seen = set()
        current = self.get(experiment_id)
        while True:
            if current.experiment_id in seen:
                raise ValueError("experiment lineage cycle detected")
            seen.add(current.experiment_id)
            chain.append(current)
            if not current.parent_id:
                break
            current = self.get(current.parent_id)
        chain.reverse()
        return chain

    def reproductions(self, experiment_id: str) -> List[Experiment]:
        self.get(experiment_id)
        return sorted(
            (exp for exp in self._experiments.values() if exp.reproduced_from == experiment_id),
            key=lambda item: item.experiment_id,
        )

    def compare_metrics(self, left_id: str, right_id: str) -> Dict[str, Dict[str, Optional[float]]]:
        left = self.get(left_id)
        right = self.get(right_id)
        keys = sorted(set(left.metrics) | set(right.metrics))
        result: Dict[str, Dict[str, Optional[float]]] = {}
        for key in keys:
            a = float(left.metrics[key]) if key in left.metrics else None
            b = float(right.metrics[key]) if key in right.metrics else None
            result[key] = {
                "left": a,
                "right": b,
                "delta": None if a is None or b is None else b - a,
            }
        return result

    def manifest(self) -> Dict[str, Any]:
        rows = []
        for exp in self.list():
            rows.append({
                "experiment_id": exp.experiment_id,
                "name": exp.name,
                "hypothesis": exp.hypothesis,
                "parent_id": exp.parent_id,
                "reproduced_from": exp.reproduced_from,
                "metrics": dict(sorted(exp.metrics.items())),
                "environment": dict(sorted(exp.environment.items())),
                "artifacts": list(exp.artifacts),
                "evidence_hash": exp.evidence_hash(),
            })
        return {"experiments": rows, "manifest_hash": _digest(rows)}


def environment_fingerprint(environment: Mapping[str, str]) -> str:
    return _digest(dict(sorted(environment.items())))
