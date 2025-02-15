#ifndef HUOBZ_EMOTION_H
#define HUOBZ_EMOTION_H

#include "../neurotransmitters/HuobzNeurotransmitter.h"
#include "../memory/HuobzMemory.h"
#include <ctime>

class HuobzEmotion {
public:
    double intensity;
    std::string type;
    HuobzNeurotransmitter* neurotransmitter;
    HuobzMemory* memory;
    time_t lastUpdated;

    HuobzEmotion(std::string emotionType, HuobzNeurotransmitter* linked_neurotransmitter, HuobzMemory* memory_system);
    
    void adjustIntensity();
    void reactToMemory(std::string memoryKey);
    void applyEmotionalDecay();
};

#endif
