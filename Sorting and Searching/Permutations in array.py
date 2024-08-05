class Solution:
    def isPossible(self, k, arr1, arr2):
        #Your code goes here.
        arr1.sort()
        arr2 = sorted(arr2)[::-1]
        n = len(arr1)
        for i in range(n):
            if arr1[i]+arr2[i] < k:
                return False
        return True
