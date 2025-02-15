#include "HuobzEmotion.h"

HuobzEmotion::HuobzEmotion(HuobzNeurotransmitter* linked_neurotransmitter) {
    neurotransmitter = linked_neurotransmitter;
    intensity = neurotransmitter->level;
}

void HuobzEmotion::adjustIntensity() {
    intensity = neurotransmitter->level;
}
