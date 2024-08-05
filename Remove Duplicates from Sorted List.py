class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            if not node.next: break
            if node.next.val==node.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
