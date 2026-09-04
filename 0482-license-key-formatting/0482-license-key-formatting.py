class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        groups = []
        while len(s) > k:
            groups.append(s[-k:])
            s = s[:-k]
        if s:
            groups.append(s)
        return "-".join(reversed(groups))