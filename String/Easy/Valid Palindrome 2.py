class Solution:
    def validPalindrome(self, s: str) -> bool:
        # beats 5% in time complexity
        lef = 0
        n = len(s)
        rit = n-1
        while lef<rit:
            print(s[lef],s[rit])
            if s[lef]==s[rit]:
                lef+=1
                rit-=1
                continue
            a = s[:lef]+s[lef+1:]
            b = s[:rit]+s[rit+1:]
            return a==a[::-1] or b==b[::-1]
        return True
