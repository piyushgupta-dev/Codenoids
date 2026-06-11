#include <string>

class Solution {
private:
    inline int romanToValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }

public:
    int romanToInt(std::string s) {
        int total = 0;
        int n = s.length();
        
        for (int i = 0; i < n; ++i) {
            int current_val = romanToValue(s[i]);
            
            if (i + 1 < n && current_val < romanToValue(s[i + 1])) {
                total -= current_val;
            } else {
                total += current_val;
            }
        }
        
        return total;
    }
};
