class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = [0] * 26

        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ord(ch) - ord('a')] += 1

        answer = " "

        for word in words:
            count = [0] * 26 

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            valid = True
            for i in range(26):
                if count[i] < need[i]:
                    valid = False
                    break

            if valid and (answer == " " or len(word) < len(answer)):
                answer = word

        return answer                           