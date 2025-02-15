#include "HuobzEmotion.h"

HuobzEmotion::HuobzEmotion(std::string emotionType, HuobzNeurotransmitter* linked_neurotransmitter, HuobzMemory* memory_system) {
    type = emotionType;
    neurotransmitter = linked_neurotransmitter;
    memory = memory_system;
    intensity = neurotransmitter->level;
    lastUpdated = time(0);
}

void HuobzEmotion::adjustIntensity() {
    intensity = neurotransmitter->level;
}

void HuobzEmotion::reactToMemory(std::string memoryKey) {
    std::string pastMemory = memory->recallLongTerm(memoryKey);
    if (pastMemory != "No long-term memory found for this key.") {
        intensity += 3.0;  // Increase emotion intensity for positive memory
    } else {
        intensity -= 1.0;  // Decay emotion if no reinforcing memory is found
    }
    lastUpdated = time(0);
}

void HuobzEmotion::applyEmotionalDecay() {
    time_t now = time(0);
    double timeElapsed = difftime(now, lastUpdated);

    if (timeElapsed > 30) {  // After 30 seconds, emotion intensity decreases
        intensity -= 2.0;
        if (intensity < 0) {
            intensity = 0;  // Emotion cannot go negative
        }
        lastUpdated = time(0);
    }
}
