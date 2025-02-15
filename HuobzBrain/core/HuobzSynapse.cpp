#include "HuobzSynapse.h"

HuobzSynapse::HuobzSynapse(HuobzNeuron* from, HuobzNeuron* to) {
    this->from = from;
    this->to = to;
    this->weight = ((double)rand() / RAND_MAX) * 2 - 1; // Random weight between -1 and 1
}

void HuobzSynapse::transmit() {
    to->activation += from->activation * weight;
}
