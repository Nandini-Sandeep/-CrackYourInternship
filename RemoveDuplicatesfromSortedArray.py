class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = sorted(list(set(nums)))
        # O(n logn)
        print(new)
        k = len(new)
        for i in range(k):
            nums[i] = new[i]
        return k
