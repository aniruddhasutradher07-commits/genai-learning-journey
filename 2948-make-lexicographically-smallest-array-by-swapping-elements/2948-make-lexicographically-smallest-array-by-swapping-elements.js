/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number[]}
 */
var lexicographicallySmallestArray = function(nums, limit) {
    const n = nums.length;

    // Store [value, originalIndex]
    const arr = nums.map((value, index) => [value, index]);

    // Sort by value
    arr.sort((a, b) => a[0] - b[0]);

    const result = new Array(n);

    let start = 0;

    while (start < n) {
        let end = start;

        // Find all values belonging to the same swappable group
        while (
            end + 1 < n &&
            arr[end + 1][0] - arr[end][0] <= limit
        ) {
            end++;
        }

        // Collect indices of this group
        const indices = [];

        for (let i = start; i <= end; i++) {
            indices.push(arr[i][1]);
        }

        // Sort original positions
        indices.sort((a, b) => a - b);

        // Values are already sorted because arr is sorted
        // Put smallest values into smallest indices
        for (let i = 0; i < indices.length; i++) {
            result[indices[i]] = arr[start + i][0];
        }

        start = end + 1;
    }

    return result;
};