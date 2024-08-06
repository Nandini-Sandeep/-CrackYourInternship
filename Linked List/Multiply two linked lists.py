class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        n1 = 0
        node = first
        while node:
            n1 = n1*10 + node.data
            node = node.next
        n2 = 0
        node = second
        while node:
            n2 = n2*10 + node.data
            node = node.next
        return (n1*n2)%(10**9 + 7)
