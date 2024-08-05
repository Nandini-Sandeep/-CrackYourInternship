class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for i in prices:
            if i<minprice:
                minprice = i
            elif i-minprice > maxprofit:
                maxprofit = i-minprice
        return maxprofit
