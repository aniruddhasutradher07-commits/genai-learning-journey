/**
 * @param {string} s
 * @param {string} target
 * @return {string}
 */
var lexPalindromicPermutation = function (s, target) {
    const n = s.length;
    const m = Math.floor(n / 2);

    const freq = Array(26).fill(0);

    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    // Check whether a palindromic permutation is possible
    let oddCount = 0;
    let middle = "";

    for (let i = 0; i < 26; i++) {
        if (freq[i] % 2 !== 0) {
            oddCount++;
            middle = String.fromCharCode(97 + i);
        }
    }

    if (oddCount > 1) return "";
    if (n % 2 === 0 && oddCount !== 0) return "";

    // Counts available for the left half
    const halfCount = Array(26).fill(0);

    for (let i = 0; i < 26; i++) {
        halfCount[i] = Math.floor(freq[i] / 2);
    }

    function buildPalindrome(left) {
        return left + middle + left.split("").reverse().join("");
    }

    function smallestSuffix(count) {
        let result = "";

        for (let i = 0; i < 26; i++) {
            if (count[i] > 0) {
                result += String.fromCharCode(97 + i).repeat(count[i]);
            }
        }

        return result;
    }

    /*
     * Try to follow target's left half as much as possible.
     */
    const remaining = [...halfCount];
    let prefix = "";

    for (let i = 0; i < m; i++) {
        const x = target.charCodeAt(i) - 97;

        if (remaining[x] > 0) {
            remaining[x]--;
            prefix += target[i];
        } else {
            break;
        }
    }

    /*
     * If we matched the complete left half, check whether
     * that exact palindrome is already greater than target.
     */
    if (prefix.length === m) {
        const candidate = buildPalindrome(prefix);

        if (candidate > target) {
            return candidate;
        }
    }

    /*
     * Find the rightmost position that can be increased.
     *
     * This guarantees the lexicographically smallest answer.
     */

    while (true) {

        const pos = prefix.length;

        // Try increasing the current unmatched position
        if (pos < m) {
            const targetChar =
                target.charCodeAt(pos) - 97;

            for (let c = targetChar + 1; c < 26; c++) {
                if (remaining[c] > 0) {

                    remaining[c]--;

                    const left =
                        prefix +
                        String.fromCharCode(97 + c) +
                        smallestSuffix(remaining);

                    return buildPalindrome(left);
                }
            }
        }

        // Cannot increase here → backtrack
        if (prefix.length === 0) {
            return "";
        }

        const last =
            prefix.charCodeAt(prefix.length - 1) - 97;

        prefix =
            prefix.slice(0, -1);

        // Restore removed character
        remaining[last]++;

        // Try replacing it with the smallest larger character
        for (let c = last + 1; c < 26; c++) {

            if (remaining[c] > 0) {

                remaining[c]--;

                const left =
                    prefix +
                    String.fromCharCode(97 + c) +
                    smallestSuffix(remaining);

                return buildPalindrome(left);
            }
        }
    }
};