class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        L = []
        node = head
        while node:
            L.append(node.val)
            node = node.next 
        # print(L)
        return L==L[::-1]
