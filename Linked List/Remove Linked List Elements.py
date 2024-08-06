class Solution:
    def removeElements(self, head: Optional[ListNode], vl: int) -> Optional[ListNode]:
        while head and head.val==vl:
            head = head.next
        if not head: return head

        node = head
        while node:
            if node.next==None:
                break
            nex = node.next
            if nex.val==vl:
                node.next = nex.next
            else:
                node = nex
        return head
