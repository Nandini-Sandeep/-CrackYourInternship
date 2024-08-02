class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        start = prices[0]
        for i in prices:
            if start < i: 
                maxp += i - start
            start = i
        return maxp
