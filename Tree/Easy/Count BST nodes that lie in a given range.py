class Solution:
    def getCount(self,root,low,high):
        def dfs(node,s=0):
            if not node: return 0
            if node.data in range(low,high+1): s = 1
            return s + dfs(node.left) + dfs(node.right)
        return dfs(root)
