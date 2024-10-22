class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(node1,node2):
            if node1: print(node1.val,end=' ')
            else: print('None',end=' ')
            if node2: print(node2.val)
            else: print('None')
            if not node1 and not node2:
                return True
            # not Null
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                return equal(node1.left,node2.left) and equal(node1.right,node2.right)
            # either one is Null
            return False

        def trav(root):
            if not root: return subRoot==None
            if equal(root,subRoot):
                return True
            L = trav(root.left)
            R = trav(root.right)
            return L or R
        
        return trav(root)
