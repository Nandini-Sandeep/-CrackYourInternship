class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node==None: return 0
            L = node.left
            # only left leaf nodes matter
            if L and not (L.left or L.right): s=L.val
            else: s = 0
            return s + dfs(node.left)+dfs(node.right)
        return dfs(root)
        
