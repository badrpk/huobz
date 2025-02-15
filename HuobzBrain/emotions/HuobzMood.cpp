#include "HuobzMood.h"

HuobzMood::HuobzMood() {}

void HuobzMood::addEmotion(HuobzEmotion* emotion) {
    emotions.push_back(emotion);
}

std::string HuobzMood::determineMood() {
    double totalIntensity = 0;
    int count = 0;

    for (auto& emotion : emotions) {
        emotion->applyEmotionalDecay();  // Apply decay before calculating
        totalIntensity += emotion->intensity;
        count++;
    }

    double averageIntensity = (count > 0) ? (totalIntensity / count) : 0;

    if (averageIntensity > 7) {
        return "Happy 😊";
    } else if (averageIntensity > 4) {
        return "Neutral 😐";
    } else {
        return "Sad 😢";
    }
}
