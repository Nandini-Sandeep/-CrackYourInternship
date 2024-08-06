class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L = []
        node = head
        while node:
            L.append(node)
            node = node.next
        n = len(L)
        return L[n//2]
        
