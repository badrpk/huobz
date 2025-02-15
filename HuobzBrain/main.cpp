#include <iostream>
#include "core/HuobzNeuron.h"
#include "core/HuobzSynapse.h"
#include "memory/HuobzMemory.h"
#include "neurotransmitters/HuobzNeurotransmitter.h"
#include "emotions/HuobzEmotion.h"
#include "emotions/HuobzMood.h"
#include <unistd.h>  // For sleep

int main() {
    HuobzNeuron n1, n2;
    HuobzSynapse s1(&n1, &n2);
    HuobzMemory memorySystem;
    HuobzNeurotransmitter dopamine(5.0);
    HuobzNeurotransmitter serotonin(6.0);

    HuobzEmotion happiness("happiness", &dopamine, &memorySystem);
    HuobzEmotion calmness("calmness", &serotonin, &memorySystem);

    HuobzMood moodSystem;
    moodSystem.addEmotion(&happiness);
    moodSystem.addEmotion(&calmness);

    // Store an emotionally significant memory
    memorySystem.storeLongTerm("promotion", "Got a job promotion!");

    // React to stored memory
    happiness.reactToMemory("promotion");

    // Determine mood before decay
    std::cout << "Initial Mood: " << moodSystem.determineMood() << std::endl;

    // Simulate time passing (30 seconds)
    sleep(30);
    std::cout << "Mood After Emotional Decay: " << moodSystem.determineMood() << std::endl;

    return 0;
}
