class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        vector<int> canMatch(n + 1);
        canMatch[n] = m;
        int p = m;
        for (int i = n - 1; i >= 0; i--) {
            if (p > 0 && word1[i] == word2[p - 1]) {
                p--;
            }
            canMatch[i] = p;
        }

        vector<int> res;
        int k = 0;
        bool used = false;

        for (int i = 0; i < n; i++) {
            if (k == m) break;
            if (word1[i] == word2[k]) {
                res.push_back(i);
                k++;
            } else if (!used && canMatch[i + 1] <= k + 1) {
                res.push_back(i);
                k++;
                used = true;
            }
        }

        return (k == m) ? res : vector<int>();
    }
};