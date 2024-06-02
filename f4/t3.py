_, cnt = [int(p) for p in input().split()]
k = [int(p) for p in input().split()]
kp = [0]
kinit = 0
for kk in k:
    kinit+=kk
    kp.append(kinit)

def sum_razd(a,b):
    global kp
    return kp[b] - kp[a]

res = []
for j in range(cnt):
    l, s = [int(p) for p in input().split()]
    
    f1 = 0
    f2 = len(k)-l+1

    while(f2-f1 > 1):
        fs = (f1+f2)//2
        # su = sum(k[fs:fs+l])
        # su = sum_razd(fs, fs+l)
        su = kp[fs+l] - kp[fs]
        if(su > s):
            f2 = fs
        else:
            f1 = fs
    # su = sum(k[f1:f1+l])
    # su = sum_razd(f1, f1+l)
    su = kp[f1+l] - kp[f1]
    if(su != s):
        res.append(-1)
    else:
        res.append(f1+1)

for a in res:
    print(a)