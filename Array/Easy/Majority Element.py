class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        D = {}
        n = len(nums)
        for i in nums:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        for i in D.keys():
            if D[i]>n/2:
                return i
        
