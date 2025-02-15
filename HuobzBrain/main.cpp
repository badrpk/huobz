#include <iostream>
#include "core/HuobzNeuron.h"
#include "core/HuobzSynapse.h"
#include "memory/HuobzMemory.h"
#include <unistd.h> // For sleep function

int main() {
    HuobzNeuron n1, n2;
    HuobzSynapse s1(&n1, &n2);
    HuobzMemory memorySystem;

    // Store in different memory types
    memorySystem.storeShortTerm("Meeting at 3 PM.");
    memorySystem.storeLongTerm("project", "Complete HuobzAI research.");
    memorySystem.storeSubconscious("self-worth", "I am capable and strong.");

    // Simulate time passing
    sleep(5);
    memorySystem.applyMemoryDecay();

    // Recall memories
    std::cout << "Short-Term Memory Recall: " << memorySystem.recallShortTerm() << std::endl;
    std::cout << "Long-Term Memory Recall: " << memorySystem.recallLongTerm("project") << std::endl;
    std::cout << "Subconscious Memory Recall: " << memorySystem.recallSubconscious("self-worth") << std::endl;

    return 0;
}
