class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node: return 
            if node.left and node.right:
                node.left, node.right = invert(node.right), invert(node.left)
                return node
            # not both
            if node.left:
                node.right = invert(node.left)
                node.left = None
                return node
            if node.right:
                node.left = invert(node.right)
                node.right = None
                return node
            # leaf node
            return node
        return invert(root)
