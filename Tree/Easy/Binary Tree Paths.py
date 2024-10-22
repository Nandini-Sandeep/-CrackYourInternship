class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def path(node, curr='',net=set()):
            if curr: curr += '->'
            curr += str(node.val)
            if node.left==None and node.right==None:
                net.add(curr)
                return net
            L = set(); R = set()
            if node.left: L = path(node.left, curr, net)
            if node.right: R = path(node.right, curr, net)
            net = net.union(L,R)
            return net
        return path(root)
