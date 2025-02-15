#ifndef HUOBZ_EMOTION_H
#define HUOBZ_EMOTION_H

#include "../neurotransmitters/HuobzNeurotransmitter.h"

class HuobzEmotion {
public:
    double intensity;
    HuobzNeurotransmitter* neurotransmitter;
    
    HuobzEmotion(HuobzNeurotransmitter* linked_neurotransmitter);
    void adjustIntensity();
};

#endif
