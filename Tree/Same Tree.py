class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def equal(node1, node2):
            if node1==None and node2==None:
                return True
            if node1 and node2:
                if node1.val!=node2.val:
                    return False
                return equal(node1.left,node2.left) and equal(node1.right,node2.right)
            return False
        return equal(p,q)
