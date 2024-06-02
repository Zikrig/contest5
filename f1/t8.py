from math import ceil, floor
def getCeil(x1,x2,l):
    ver1 = (x1+x2)/l
    ver2 = (x1-x2)/l
    # print(ver1, ver2)
    return [
        [floor(ver1), ceil(ver1)],
        [floor(ver2), ceil(ver2)]
    ]

def getMinT(l, x1, v1, x2, v2):
    if l == 0:
        return -1
    
    if(x1 == x2):
        return 0
    
    [f1, c1], [f2, c2] = getCeil(x1, x2, l)

    # print (f1, c1, f2, c2)
    t = -1.0

    for k_possible in [f1, c1]:
        if((v1 + v2) == 0):
            # print(f'break тк {v1}+{v2} = 0')
            break
        t_possible = (k_possible *  l - x1 - x2) / ((v1 + v2))
        # print(f'Возможный t1 {t_possible}')
        if((t_possible < t or t < 0) and t_possible > 0):
            t = t_possible
    
    for k_possible in [f2, c2]:
        if(v1 == v2):
            # print(f'break тк {v1}-{v2} = 0')
            break
        t_possible = (k_possible * l - x1 + x2) / ((v1 - v2))
        # print(f'Возможный t2 {t_possible}')
        if((t_possible < t or t < 0) and t_possible > 0):
            t = t_possible

    return t

    


L, X1, V1, X2, V2 = input().split()

l = int(L)
x1 = int(X1)
v1 = int(V1)
x2 = int(X2)
v2 = int(V2)

res = getMinT(l,x1,v1,x2,v2)

if res == -1.0:
    print("NO")
else:
    print("YES")
    print(res)