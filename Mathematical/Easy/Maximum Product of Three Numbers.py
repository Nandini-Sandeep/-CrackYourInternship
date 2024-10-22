class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pos=0; neg=0
        if nums[-1]<=0:
            # all negative
            return nums[-1]*nums[-2]*nums[-3]
        if nums[-3]>0:
            pos = nums[-1]*nums[-2]*nums[-3]
            neg = nums[-1]*nums[0]*nums[1]
            return max(pos,neg)
        else:
            return nums[-1]*nums[0]*nums[1]
