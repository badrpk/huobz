#include "HuobzNeurotransmitter.h"

HuobzNeurotransmitter::HuobzNeurotransmitter(double initial_level) {
    level = initial_level;
}

void HuobzNeurotransmitter::increase(double amount) {
    level += amount;
}

void HuobzNeurotransmitter::decrease(double amount) {
    level -= amount;
}
