from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)
        
        if n < total_len:
            return []
        
        need = Counter(words)
        result = []
        
        for offset in range(word_len):
            left = offset
            count = 0
            window_count = Counter()
            
            right = offset
            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len
                
                if word not in need:
                    window_count.clear()
                    count = 0
                    left = right
                else:
                    window_count[word] += 1
                    count += 1
                    
                    while window_count[word] > need[word]:
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        count -= 1
                        left += word_len
        
        return result