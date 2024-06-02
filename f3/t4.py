def yrn(a):
    global l
    setl = set(l)
    lenl = len(l)
    if(a>=lenl):
        return lenl != len(setl)
    
    # dig = {i:0 for i in setl}
    dig = {}
    for d in l[:a]:
        if(d in dig):
            dig[d] += 1
        else:
            dig[d] = 1

    for i in range(a,lenl):
        if(l[i] in dig):
            dig[l[i]] += 1
        else:
            dig[l[i]] = 1
            
        if(dig[l[i]]>1):
            return True
        dig[l[i-a]] -= 1
        if(dig[l[i-a]]==0):
            dig.pop(l[i-a])
            
    return False
__, astr = input().split()
a = int(astr)

l  = [int(i) for i in input().split()]

res = 'YES' if yrn(a) else 'NO'
print(res)