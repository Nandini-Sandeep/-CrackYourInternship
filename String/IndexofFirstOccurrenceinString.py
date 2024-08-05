class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack); x = len(needle)
        if n==x:
            if needle==haystack:
                return 0
            else:
                return -1
        if x>n:
            return -1
        
        for i in range(n-x+1):
            if haystack[i]==needle[0]:
                if haystack[i:i+x]==needle:
                    return i
        return -1
        
