class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n = len(nums2)
        for x in nums1:
            for j in range(n):
                if nums2[j]==x:
                    break
            if j+1==n:
                ans.append(-1)
                continue
            for i in range(j,n):
                if nums2[i]>x:
                    break
            if nums2[i]<=x:
                ans.append(-1)
            else:
                ans.append(nums2[i])
        return ans
