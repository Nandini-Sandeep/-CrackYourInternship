class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(arr):
            n = len(arr)
            if n==0: return None
            if n==1: return TreeNode(arr[0])
            mid = n//2
            left = tree(arr[:mid])
            right = tree(arr[mid+1:])
            return TreeNode(arr[mid], left, right)
        return tree(nums)
