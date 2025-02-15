#ifndef HUOBZ_EMOTION_H
#define HUOBZ_EMOTION_H

#include "../neurotransmitters/HuobzNeurotransmitter.h"
#include "../memory/HuobzMemory.h"

class HuobzEmotion {
public:
    double intensity;
    HuobzNeurotransmitter* neurotransmitter;
    HuobzMemory* memory;

    HuobzEmotion(HuobzNeurotransmitter* linked_neurotransmitter, HuobzMemory* memory_system);
    void adjustIntensity();
    void reactToMemory(std::string memoryKey);
};

#endif
