#include "HuobzEmotion.h"

HuobzEmotion::HuobzEmotion(HuobzNeurotransmitter* linked_neurotransmitter, HuobzMemory* memory_system) {
    neurotransmitter = linked_neurotransmitter;
    memory = memory_system;
    intensity = neurotransmitter->level;
}

void HuobzEmotion::adjustIntensity() {
    intensity = neurotransmitter->level;
}

// React to past memory (increase or decrease intensity)
void HuobzEmotion::reactToMemory(std::string memoryKey) {
    std::string pastMemory = memory->recallLongTerm(memoryKey);
    if (pastMemory != "No long-term memory found for this key.") {
        intensity += 2.0;  // Increase emotion intensity when recalling a significant memory
    } else {
        intensity -= 1.0;  // Decay emotion if no reinforcing memory is found
    }
}
