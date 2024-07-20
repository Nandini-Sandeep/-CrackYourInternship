class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # first attempt
        # n log n
        maxprice = float('-inf')
        n = len(prices)

        p = [0]*n # make list of maxprices ahead
        for i in range (n-2,-1,-1) :
            maxprice = max(maxprice,prices[i+1]) 
            p[i] = maxprice 

        maxprofit = 0 
        # subtract maxprice from smallest element
        for i in range (n-1) :
            maxprofit = max(maxprofit,p[i] - prices[i])
        return maxprofit

        '''

        minprice = prices[0]
        maxprofit = 0
        for i in prices:
            if i<minprice:
                minprice = i
            elif i-minprice > maxprofit:
                maxprofit = i-minprice
        return maxprofit
