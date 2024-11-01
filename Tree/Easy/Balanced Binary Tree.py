class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node==None: return (True,0)
            L = dfs(node.left)
            R = dfs(node.right)
            h = max(L[1],R[1])
            if L[0] and R[0] and abs(L[1]-R[1])<=1:
                return (True,h+1)
            else:
                return (False,h+1)
        return dfs(root)[0]
