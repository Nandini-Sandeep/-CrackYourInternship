class Solution:
    def climbStairs(self, n: int, D={}) -> int:
        print("doing",n)
        if n<=3:
            D[n]=n
            return n
        a, b = n-1, n-2
        if a in D and b in D:
            D[n] = D[a] + D[b]
            return D[n]
        if a in D: 
            # b not in D
            D[n] = D[a] + self.climbStairs(b,D)
            return D[n]
        if b in D: 
            # a not in D
            D[n] = self.climbStairs(a,D) + D[b]
            return D[n]
        else:
            return self.climbStairs(n-1,D) + self.climbStairs(n-2,D)
