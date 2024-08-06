class Solution:
    def compute(self,head):
        #Your code here
        L = []
        while head.next and head.data<head.next.data:
            head = head.next
        if not head: return head
        
        node = head
        while node:
            v = node.data
            while L and L[-1].data<v:
                L.pop()
            L.append(node)
            node = node.next
        
        head = L[0]
        node = head
        for i in L[1:]:
            node.next = i
            node = node.next
        return head
