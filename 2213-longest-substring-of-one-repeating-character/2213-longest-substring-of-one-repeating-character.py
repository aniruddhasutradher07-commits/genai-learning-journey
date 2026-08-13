from typing import List


class Node:
    __slots__ = ("length", "pref", "suf", "best", "lch", "rch")

    def __init__(self, length=0, pref=0, suf=0, best=0, lch="", rch=""):
        self.length = length
        self.pref = pref
        self.suf = suf
        self.best = best
        self.lch = lch
        self.rch = rch


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        n = len(s)
        s = list(s)
        tree = [Node() for _ in range(4 * n)]

        def build(node: int, l: int, r: int) -> None:
            if l == r:
                tree[node] = Node(1, 1, 1, 1, s[l], s[l])
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def merge(left: Node, right: Node) -> Node:
            res = Node()
            res.length = left.length + right.length
            res.lch = left.lch
            res.rch = right.rch

            res.pref = left.pref
            if left.pref == left.length and left.rch == right.lch:
                res.pref += right.pref

            res.suf = right.suf
            if right.suf == right.length and right.lch == left.rch:
                res.suf += left.suf

            res.best = max(left.best, right.best)
            if left.rch == right.lch:
                res.best = max(res.best, left.suf + right.pref)

            return res

        def update(node: int, l: int, r: int, idx: int, ch: str) -> None:
            if l == r:
                tree[node] = Node(1, 1, 1, 1, ch, ch)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)

        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            if s[idx] != ch:
                s[idx] = ch
                update(1, 0, n - 1, idx, ch)
            ans.append(tree[1].best)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestRepeating("babacc", "bcb", [1, 3, 3])) 
    print(sol.longestRepeating("abyzz", "aa", [2, 1]))        