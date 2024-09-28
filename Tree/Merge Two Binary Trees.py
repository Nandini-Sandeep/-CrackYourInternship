class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(nod1, nod2):
            if nod1==None and nod2==None:
                return None
            if nod1==None: return nod2
            if nod2==None: return nod1
            left = merge(nod1.left, nod2.left)
            right = merge(nod1.right, nod2.right)
            nval = nod1.val + nod2.val
            return TreeNode(nval, left, right)
        return merge(root1, root2)
