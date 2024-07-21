class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brack = {'(':')',')':'(','{':'}','}':'{','[':']',']':'['}
        if len(s)%2: return False
        for b in s:
            if b in '({[':
                stack.append(b)
            else:
                if stack==[] or stack[-1]!=brack[b]: return False
                stack.pop()
        if stack: return False
        return True
