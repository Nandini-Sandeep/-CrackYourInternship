class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        node = headA
        while node:
            s.add(node)
            node = node.next
        node = headB
        while node:
            if node in s:
                return node
            node = node.next
