class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        product = 1
        has0 = 0
        for i in nums:
            if i==0: has0 += 1
            else: product *= i
        if has0 > 1: return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]==0: 
                ans[i] = product 
                continue
            if has0:ans[i] = 0
            else: ans[i] = product//nums[i]
        return ans
