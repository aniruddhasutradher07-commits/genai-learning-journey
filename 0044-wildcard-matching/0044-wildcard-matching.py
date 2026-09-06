class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        star_idx = -1
        match_idx = 0

        len_s, len_p = len(s), len(p)

        while s_idx < len_s:
            if p_idx < len_p and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1

            elif p_idx < len_p and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1

            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx

            else:
                return False

        while p_idx < len_p and p[p_idx] == '*':
            p_idx += 1

        return p_idx == len_p                        