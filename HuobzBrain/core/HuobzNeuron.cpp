#include "HuobzNeuron.h"
#include <cstdlib>
#include <ctime>

HuobzNeuron::HuobzNeuron() {
    bias = ((double)rand() / RAND_MAX) * 2 - 1; // Random bias between -1 and 1
    activation = 0.0;
}

void HuobzNeuron::connect(HuobzNeuron* neuron) {
    connections.push_back(neuron);
}

void HuobzNeuron::fire() {
    double sum = bias;
    for (auto& neuron : connections) {
        sum += neuron->activation;
    }
    activation = 1 / (1 + exp(-sum)); // Sigmoid Activation Function
}
