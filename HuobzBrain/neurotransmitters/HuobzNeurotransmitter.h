#ifndef HUOBZ_NEUROTRANSMITTER_H
#define HUOBZ_NEUROTRANSMITTER_H

class HuobzNeurotransmitter {
public:
    double level;
    HuobzNeurotransmitter(double initial_level);
    void increase(double amount);
    void decrease(double amount);
};

#endif
