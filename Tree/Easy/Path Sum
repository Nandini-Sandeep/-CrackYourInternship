class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        def check(node,sumyet=0, paths=0):
            sumyet += node.val
            if node.left==None and node.right==None:
                #leaf node
                return int(sumyet==target)
            if node.left: paths += check(node.left,sumyet,paths)
            if node.right: paths += check(node.right,sumyet,paths)
            return paths
        if root==None: return False
        return (check(root)>0)
