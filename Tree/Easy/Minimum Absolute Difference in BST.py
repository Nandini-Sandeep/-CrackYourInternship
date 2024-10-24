# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        def read(node):
            if node.left: read(node.left)
            if node.right: read(node.right)
            vals.append(node.val)
            return
        read(root)
        vals.sort()
        diffs = []
        for i in range(len(vals)-1):
            diffs.append(vals[i+1]-vals[i])
        return (min(diffs))
