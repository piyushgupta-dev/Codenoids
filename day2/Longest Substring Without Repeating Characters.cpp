#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::vector<int> charMap(256, -1);
        return solveRecursive(s, 0, 0, 0, charMap);
    }

private:
    int solveRecursive(const std::string& s, int left, int right, int maxLen, std::vector<int>& charMap) {
        if (right == s.length()) {
            return maxLen;
        }

        unsigned char currentChar = s[right];
        if (charMap[currentChar] >= left) {
            left = charMap[currentChar] + 1;
        }

        charMap[currentChar] = right;

        int currentLen = right - left + 1;
        maxLen = std::max(maxLen, currentLen);

        return solveRecursive(s, left, right + 1, maxLen, charMap);
    }
};
