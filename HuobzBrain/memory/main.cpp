#include <iostream>
#include "core/HuobzNeuron.h"
#include "core/HuobzSynapse.h"
#include "memory/HuobzMemory.h"

int main() {
    HuobzNeuron n1, n2;
    HuobzSynapse s1(&n1, &n2);
    HuobzMemory memorySystem;

    // Store & recall short-term memory
    memorySystem.storeShortTerm("Remember to eat.");
    memorySystem.storeShortTerm("Tomorrow is an important day.");
    std::cout << "Short-Term Memory Recall: " << memorySystem.recallShortTerm() << std::endl;

    // Store & recall long-term memory
    memorySystem.storeLongTerm("physics", "E=mc^2 is Einstein's theory.");
    std::cout << "Long-Term Memory Recall: " << memorySystem.recallLongTerm("physics") << std::endl;

    return 0;
}
