def duplicates(s):
    D = {}
    for i in s:
        if i in D: D[i]+=1
        else: D[i] = 1
    for i in D:
        print(i,'count =',D[i])
    return
