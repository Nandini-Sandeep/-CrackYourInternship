class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L = []
        node = head
        while node:
            L.append(node)
            node = node.next
        if not L: return None
        head = L[-1]
        node = head
        L[0].next = None
        for i in range(len(L)-2,-1,-1):
            node.next = L[i]
            node = node.next
        
        return head
