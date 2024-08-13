# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def maxpath(node):
            # return u-path, s-path
            u=0; s=0
            if node.left and node.right:
                L = maxpath(node.left)
                R = maxpath(node.right)
                u = L[1]+R[1]+2
                s = max(L[1],R[1])+1
                a = max(u,s,L[0],R[0])
                ans[0] = max(ans[0],a)
                return (u,s)
            # not both
            if node.left:
                L = maxpath(node.left)
                u = 0
                s = L[1] + 1
                a = s
                ans[0] = max(ans[0], a)
                return (u,s)
            if node.right:
                R = maxpath(node.right)
                u = 0
                s = R[1] + 1
                a = s
                ans[0] = max(ans[0], a)
                return (u,s)
            # else leaf node
            return (0,0)
        maxpath(root)
        return ans[0]
