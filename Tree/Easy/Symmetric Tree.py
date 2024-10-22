class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def equal(node1, node2):
            if node1==None and node2==None:
                return True
            if node1 and node2:
                if node1.val!=node2.val:
                    return False
                return equal(node1.left,node2.right) and equal(node1.right,node2.left)
            return False
        return equal(root.left,root.right)
