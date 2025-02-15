#ifndef HUOBZ_SYNAPSE_H
#define HUOBZ_SYNAPSE_H

#include "HuobzNeuron.h"

class HuobzSynapse {
public:
    HuobzNeuron* from;
    HuobzNeuron* to;
    double weight;
    
    HuobzSynapse(HuobzNeuron* from, HuobzNeuron* to);
    void transmit();
};

#endif
