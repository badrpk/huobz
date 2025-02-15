#include <iostream>
#include "core/HuobzNeuron.h"
#include "core/HuobzSynapse.h"
#include "emotions/HuobzEmotion.h"
#include "neurotransmitters/HuobzNeurotransmitter.h"

int main() {
    HuobzNeuron n1, n2;
    HuobzSynapse s1(&n1, &n2);
    HuobzNeurotransmitter dopamine(5.0);
    HuobzEmotion happiness(&dopamine);

    n1.activation = 1.0;
    s1.transmit();
    n2.fire();

    dopamine.increase(2.0);
    happiness.adjustIntensity();

    std::cout << "Neuron 2 Activation: " << n2.activation << std::endl;
    std::cout << "Happiness Intensity: " << happiness.intensity << std::endl;

    return 0;
}
