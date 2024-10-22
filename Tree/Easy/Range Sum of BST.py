class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        netsum = 0
        def fs(node):
            if node==None: return 0
            sum1 = fs(node.right) + fs(node.left)
            if node.val>=low and node.val<=high:
                sum1 += node.val
            return sum1
        return fs(root)
