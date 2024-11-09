class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0]*(n+1)
        for i in range(1,n+1):
            if i<3: steps[i] = i
            else: steps[i] = steps[i-1] + steps[i-2]
        return steps[n]
