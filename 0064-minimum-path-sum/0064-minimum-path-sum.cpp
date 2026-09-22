#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        // 1D DP array initialized to store row minimum sums
        vector<int> dp(n, 0);
        
        dp[0] = grid[0][0];
        // Initialize the first row
        for (int c = 1; c < n; ++c) {
            dp[c] = dp[c - 1] + grid[0][c];
        }
        
        // Fill for remaining rows
        for (int r = 1; r < m; ++r) {
            dp[0] += grid[r][0]; // First column update
            for (int c = 1; c < n; ++c) {
                dp[c] = grid[r][c] + min(dp[c], dp[c - 1]);
            }
        }
        
        return dp[n - 1];
    }
};