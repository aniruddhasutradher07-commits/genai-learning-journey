class Solution:
    def mostWordsFound(self, sentences):
        ans = 0

        for sentence in sentences:
            words = sentence.count(" ") + 1
            ans = max(ans, words)

        return ans