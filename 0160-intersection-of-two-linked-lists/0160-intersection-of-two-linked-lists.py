class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA