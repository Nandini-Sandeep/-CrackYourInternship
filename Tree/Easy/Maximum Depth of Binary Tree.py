class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node==None: return 0
            if node.left==None and node.right==None: return 1
            if node.left and node.right:
                return max(dfs(node.left), dfs(node.right)) + 1
            if node.left: return dfs(node.left) + 1
            else: return dfs(node.right) + 1
        return dfs(root)
            
