#include <vector>

using namespace std;

class SegmentTree {
private:
    int n;
    int k;
    vector<int> tree_prod;
    vector<vector<int>> tree_cnt;

    void merge(int node, int left_node, int right_node) {
        // Merge product modulo k
        tree_prod[node] = (tree_prod[left_node] * tree_prod[right_node]) % k;

        // Reset current node counts
        for (int r = 0; r < k; ++r) {
            tree_cnt[node][r] = 0;
        }

        // Prefixes entirely contained in the left child
        for (int r = 0; r < k; ++r) {
            tree_cnt[node][r] += tree_cnt[left_node][r];
        }

        // Prefixes extending into the right child
        int left_prod = tree_prod[left_node];
        for (int r = 0; r < k; ++r) {
            int new_rem = (left_prod * r) % k;
            tree_cnt[node][new_rem] += tree_cnt[right_node][r];
        }
    }

    void build(const vector<int>& nums, int node, int start, int end) {
        if (start == end) {
            int val_mod = nums[start] % k;
            tree_prod[node] = val_mod;
            tree_cnt[node][val_mod] = 1;
            return;
        }

        int mid = start + (end - start) / 2;
        int left_node = 2 * node;
        int right_node = 2 * node + 1;

        build(nums, left_node, start, mid);
        build(nums, right_node, mid + 1, end);
        merge(node, left_node, right_node);
    }

public:
    SegmentTree(const vector<int>& nums, int k_val) {
        n = nums.size();
        k = k_val;
        tree_prod.resize(4 * n, 1);
        tree_cnt.resize(4 * n, vector<int>(k, 0));
        build(nums, 1, 0, n - 1);
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            int val_mod = val % k;
            tree_prod[node] = val_mod;
            fill(tree_cnt[node].begin(), tree_cnt[node].end(), 0);
            tree_cnt[node][val_mod] = 1;
            return;
        }

        int mid = start + (end - start) / 2;
        int left_node = 2 * node;
        int right_node = 2 * node + 1;

        if (idx <= mid) {
            update(left_node, start, mid, idx, val);
        } else {
            update(right_node, mid + 1, end, idx, val);
        }
        merge(node, left_node, right_node);
    }

    pair<int, int> query(int node, int start, int end, int L, int R, int curr_prod, int target_x) {
        if (L <= start && end <= R) {
            int count = 0;
            for (int r = 0; r < k; ++r) {
                if ((curr_prod * r) % k == target_x) {
                    count += tree_cnt[node][r];
                }
            }
            int new_prod = (curr_prod * tree_prod[node]) % k;
            return {count, new_prod};
        }

        int mid = start + (end - start) / 2;
        int left_node = 2 * node;
        int right_node = 2 * node + 1;

        int res_count = 0;

        if (L <= mid) {
            auto [left_cnt, next_prod] = query(left_node, start, mid, L, R, curr_prod, target_x);
            res_count += left_cnt;
            curr_prod = next_prod;
        }
        if (R > mid) {
            auto [right_cnt, next_prod] = query(right_node, mid + 1, end, L, R, curr_prod, target_x);
            res_count += right_cnt;
            curr_prod = next_prod;
        }

        return {res_count, curr_prod};
    }
};

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        SegmentTree seg_tree(nums, k);
        vector<int> result;
        result.reserve(queries.size());

        for (const auto& q : queries) {
            int index_i = q[0];
            int value_i = q[1];
            int start_i = q[2];
            int x_i = q[3];

            seg_tree.update(1, 0, n - 1, index_i, value_i);
            auto [ans_cnt, _] = seg_tree.query(1, 0, n - 1, start_i, n - 1, 1, x_i);
            result.push_back(ans_cnt);
        }

        return result;
    }
};