#include <string>
#include <algorithm>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        if (s.empty()) return "";
        
        int n = s.length();
        int start = 0, maxLen = 1;

        for (int i = 0; i < 2 * n - 1; ++i) {
            int left = i / 2;
            int right = (i + 1) / 2;

            while (left >= 0 && right < n && s[left] == s[right]) {
                int currentLen = right - left + 1;
                if (currentLen > maxLen) {
                    maxLen = currentLen;
                    start = left;
                }
                left--;
                right++;
            }
        }

        return s.substr(start, maxLen);
    }
};
