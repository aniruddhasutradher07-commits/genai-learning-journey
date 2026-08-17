class Solution {
public:
    int n;
    vector<long long>pre;
    vector<vector<int>>memo;

    long long rangeSum(int i, int j) {
        return pre[j + 1] - pre[i];
    }

    int solve(int i, int j) {
        if (i == j) return 0;
        if (memo[i][j] != -1) return memo[i][j];

        int best = 0;
        for (int k = i; k < j; k++) {
            long long leftSum = rangeSum(i, k);
            long long rightSum = rangeSum(k + 1, j);

            int score;
            if (leftSum < rightSum) {
                score = (int)leftSum + solve(i, k);
            } else if (leftSum > rightSum) {
                score = (int)rightSum + solve(k + 1, j);
            } else {
                score = (int)leftSum + max(solve(i, k), solve(k + 1, j));
            }
            best = max(best, score);
        }
        return memo[i][j] = best;
    }

    int stoneGameV(vector<int>& stoneValue) {
        n = stoneValue.size();
        pre.assign(n + 1, 0);
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + stoneValue[i];
        memo.assign(n, vector<int>(n, -1));
        return solve(0, n - 1);
    }    
};