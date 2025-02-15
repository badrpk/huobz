#ifndef HUOBZ_NEURON_H
#define HUOBZ_NEURON_H

#include <vector>
#include <cmath>
#include <random>

class HuobzNeuron {
public:
    double activation;
    std::vector<HuobzNeuron*> connections;
    double bias;
    
    HuobzNeuron();
    void connect(HuobzNeuron* neuron);
    void fire();
};

#endif
