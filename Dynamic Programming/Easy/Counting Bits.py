class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            a = str(bin(i))
            #print(a)
            ans.append(a.count('1'))
        return ans
