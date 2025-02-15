#include "HuobzMemory.h"

HuobzMemory::HuobzMemory() {}

// Store in Short-Term Memory (STM) with timestamp
void HuobzMemory::storeShortTerm(std::string data) {
    time_t now = time(0);
    if (shortTermMemory.size() >= 5) {
        shortTermMemory.erase(shortTermMemory.begin()); // Remove oldest if full
    }
    shortTermMemory.push_back({data, now});
}

// Store in Long-Term Memory (LTM) with timestamp
void HuobzMemory::storeLongTerm(std::string key, std::string data) {
    time_t now = time(0);
    longTermMemory[key] = {data, now};
}

// Store in Subconscious Memory (Persists indefinitely)
void HuobzMemory::storeSubconscious(std::string key, std::string data) {
    subconsciousMemory[key] = data;
}

// Retrieve from Short-Term Memory
std::string HuobzMemory::recallShortTerm() {
    return shortTermMemory.empty() ? "No short-term memory found." : shortTermMemory.back().first;
}

// Retrieve from Long-Term Memory
std::string HuobzMemory::recallLongTerm(std::string key) {
    return longTermMemory.count(key) ? longTermMemory[key].first : "No long-term memory found for this key.";
}

// Retrieve from Subconscious Memory
std::string HuobzMemory::recallSubconscious(std::string key) {
    return subconsciousMemory.count(key) ? subconsciousMemory[key] : "No subconscious memory found.";
}

// Simulate Memory Decay Over Time
void HuobzMemory::applyMemoryDecay() {
    time_t now = time(0);
    // Remove STM items older than 30 seconds
    while (!shortTermMemory.empty() && (now - shortTermMemory.front().second > 30)) {
        shortTermMemory.erase(shortTermMemory.begin());
    }
    // Remove LTM items older than 10 minutes
    for (auto it = longTermMemory.begin(); it != longTermMemory.end();) {
        if (now - it->second.second > 600) {
            it = longTermMemory.erase(it);
        } else {
            ++it;
        }
    }
}
