class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int minOdd = INT_MAX;
        bool hasOdd = false;

        for (int x : nums1) {
            if (x % 2 == 1) {
                minOdd = min(minOdd, x);
                hasOdd = true;
            }
        }

        if (!hasOdd)
            return true;

        for (int x : nums1) {
            if (x % 2 == 0 && x < minOdd) {
                return false;
            }
        }

        return true;
    }
};