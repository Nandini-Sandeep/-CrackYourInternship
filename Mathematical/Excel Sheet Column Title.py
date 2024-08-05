class Solution:
    def convertToTitle(self, cn: int) -> str:
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        pw=26
        while cn>0:
            cn -= 1
            ans = s[cn%26] + ans
            # print(cn,ans)
            cn = cn//26
        return ans
