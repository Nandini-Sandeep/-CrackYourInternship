def findMedian(root):
    def dfs(node):
        if not node: return []
        return dfs(node.left) + [node.data] + dfs(node.right)
    s = dfs(root)
    n = len(s)
    #print(s)
    #print((n+1)//2)
    if n%2: ans = s[ (n-1)//2 ]
    else: ans = ( s[n//2] + s[n//2 -1] )/2
    if int(ans)==ans: return int(ans)
    else: return ans
