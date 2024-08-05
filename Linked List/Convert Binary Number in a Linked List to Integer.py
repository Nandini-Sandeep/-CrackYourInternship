class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = ''
        node = head
        while node:
            b += str(node.val)
            node = node.next
        return int(b,2)
