class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S = ''; T = ''
        for i in s:
            if i=='#': S = S[:-1]
            else: S += i
        for i in t:
            if i=='#': T = T[:-1]
            else: T += i
        return S==T
