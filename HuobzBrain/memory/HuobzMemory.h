#ifndef HUOBZ_MEMORY_H
#define HUOBZ_MEMORY_H

#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <ctime>

class HuobzMemory {
public:
    std::vector<std::pair<std::string, time_t>> shortTermMemory;
    std::unordered_map<std::string, std::pair<std::string, time_t>> longTermMemory;
    std::unordered_map<std::string, std::string> subconsciousMemory;

    HuobzMemory();
    
    void storeShortTerm(std::string data);
    void storeLongTerm(std::string key, std::string data);
    void storeSubconscious(std::string key, std::string data);

    std::string recallShortTerm();
    std::string recallLongTerm(std::string key);
    std::string recallSubconscious(std::string key);

    void applyMemoryDecay();
};

#endif
