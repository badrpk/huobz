#ifndef HUOBZ_MOOD_H
#define HUOBZ_MOOD_H

#include "HuobzEmotion.h"
#include <vector>

class HuobzMood {
public:
    std::vector<HuobzEmotion*> emotions;

    HuobzMood();
    void addEmotion(HuobzEmotion* emotion);
    std::string determineMood();
};

#endif
