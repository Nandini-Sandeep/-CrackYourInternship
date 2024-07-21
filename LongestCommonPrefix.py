class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        minlen = len(strs[0])
        if len(strs)==1: return strs[0] # base case
        for i in strs:
            minlen = min(minlen,len(i))
        if minlen==0: return "" # base case
        for i in range(minlen):
            print('ans',ans)
            # i is the index compared in all strings
            for s in strs:
                if s[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans
