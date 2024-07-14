class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        D = {}
        for i in nums:
            if i in D:
                return i
            else:
                D[i]=1
        
