#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.length();
        vector<int> count(26, 0);
        for (char c : s) count[c - 'a']++;

        // Try every possible common prefix length i from n-1 down to 0
        for (int i = n - 1; i >= 0; --i) {
            // Check if target[0...i-1] can be built from s
            vector<int> currentCount = count;
            bool possible = true;
            for (int j = 0; j < i; ++j) {
                if (--currentCount[target[j] - 'a'] < 0) {
                    possible = false;
                    break;
                }
            }

            if (!possible) continue;

            // Find the smallest character strictly greater than target[i]
            int targetChar = target[i] - 'a';
            for (int ch = targetChar + 1; ch < 26; ++ch) {
                if (currentCount[ch] > 0) {
                    // Valid divergence point found! Construct the result.
                    currentCount[ch]--;
                    string result = target.substr(0, i);
                    result += (char)('a' + ch);

                    // Append all remaining characters in ascending order
                    for (int c = 0; c < 26; ++c) {
                        result.append(currentCount[c], 'a' + c);
                    }
                    return result;
                }
            }
        }

        return "";
    }
};