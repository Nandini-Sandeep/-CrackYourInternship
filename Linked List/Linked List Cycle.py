# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        nodes=set()
        while node:
            # print(node)
            if node in nodes: return True
            nodes.add(node)
            node = node.next
        return False
