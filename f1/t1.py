def get_common(x1, x2, k1, k2):
    if(x1<k1):
        a1, a2 = x1, x2
        x1, x2 = k1, k2
        k1, k2 = a1, a2

    if(x2<k1 or x1>k2):
        return 0
    if x2<=k2:
        return(x2-x1 + 1)
    return(k2-x1 + 1)
    

def get_all_sum_of_trees(p,v,q,m):
    x1 = p-v
    x2 = p+v
    k1 = q-m
    k2 = q+m

    x_len = x2-x1 + 1
    k_len = k2-k1 + 1

    common = get_common(x1,x2,k1,k2)

    return x_len + k_len - common

P, V = input().split()
Q, M = input().split()

print(get_all_sum_of_trees(int(P), int(V), int(Q), int(M)))