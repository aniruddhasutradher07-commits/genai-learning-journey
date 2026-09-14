class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        ans = []

        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])

            common = len(setA & setB)
            ans.append(common)

        return ans    