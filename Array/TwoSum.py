class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        '''for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]'''
        D = {}
        for i in range(n):
            x = nums[i]
            if x==target/2:
                if x in D: return [i,D[x]]
            # this should handle the duplicate situation
            need = target-x
            D[need]=i
        for i in range(n):
            if nums[i]==target/2: continue
            if nums[i] in D:
                return [i,D[nums[i]]]
