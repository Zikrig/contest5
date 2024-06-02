def get_profit(n,k, d):
    if(k<=0):
            return '-1'
    if k in [1, 2, 5]:
        return str(n) + ''.join([str(k) for dItem in range(d)])
    if k == 10:
        return str(n) + ''.join(['0' for dItem in range(d)])

    ni = int(n)
    d0 = 0
    res = str(n)
    # ds = []
    while(d0 < d):
        d0 += 1
        ni = int(ni*10) % k
        # print(ni)
        p = k - ni
        # print(p)
        if ni == 0:
            return res + ''.join(['0' for dItem in range(d0-1,d)])
        if(p < 10 and p>=0):
            res += str(p)
            ni = ni + p
        else:
            return '-1'
    return res
                

N, K, D = input().split()

print(get_profit(
    int(N),
    int(K),
    int(D)
))