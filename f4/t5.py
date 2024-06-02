def get_from_cluster(cluster_len, pos):
    p = pos+1
    if(pos > cluster_len//2):
        pos = cluster_len - pos - 1
    pos+=1
    return pos

def get_cluster_len(number):
    number += 1
    return 4*number + 1

def of_cluster(n):
    cluster_item = 2*(n**2) + 3*n
    return cluster_item

def of_cluster0(n):
    cluster_item = 2*(n**2) + n +1
    return cluster_item

def clusterize2(n):
    if(n == 0):
        return 1
    n-=1
    k1 = 0
    k2 = 10000000000000000000
    while k2-k1 > 1:
        ks = (k1+k2) // 2
        cluster_item = of_cluster(ks)
        if(cluster_item > n):
            k2 = ks
        else:
            k1 = ks
    cluster_item = of_cluster(k1)
    pos = n - of_cluster(k1)
    cluster_len = get_cluster_len(k1)
    znach = get_from_cluster(cluster_len, pos)
    return znach

def clusterize(n):
    n+=1
    k1 = 0
    k2 = 10000000000000000000
    while k2-k1 > 1:
        ks = (k1+k2) // 2
        cluster_item = of_cluster0(ks)
        if(cluster_item > n):
            k2 = ks
        else:
            k1 = ks
    cluster_item = of_cluster0(k1)
    pos = n - of_cluster0(k1)
    cluster_len = get_cluster_len(k1) -2
    znach = get_from_cluster(cluster_len, pos)
    return znach

i = int(input())-1
a = clusterize(i)
b = clusterize2(i)
print(f'{a}/{b}')