#include <iostream>
#include "core/HuobzNeuron.h"
#include "core/HuobzSynapse.h"
#include "memory/HuobzMemory.h"
#include "neurotransmitters/HuobzNeurotransmitter.h"
#include "emotions/HuobzEmotion.h"

int main() {
    HuobzNeuron n1, n2;
    HuobzSynapse s1(&n1, &n2);
    HuobzMemory memorySystem;
    HuobzNeurotransmitter dopamine(5.0);
    HuobzEmotion happiness(&dopamine, &memorySystem);

    // Store an emotionally significant memory
    memorySystem.storeLongTerm("first_success", "Winning the coding competition.");

    // React to stored memory
    happiness.reactToMemory("first_success");
    
    std::cout << "Emotion Intensity After Memory Recall: " << happiness.intensity << std::endl;

    return 0;
}
