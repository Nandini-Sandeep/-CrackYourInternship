from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        arr.sort()
        # sliding window
        i = 0
        j = 1
        while i<n and j<n:
            diff = arr[j]-arr[i]
            if i!=j and diff==x: return 1
            if diff<x: j+=1
            else: i+=1
            #print(i,j,diff)
        return -1
