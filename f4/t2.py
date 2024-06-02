
def mag(k):
    a = -1 + k * (k+2) * (k+1) // 2 - k * (k+1)*(2*k + 1) // 6
    # print(a)
    return int(a)

n = int(input())
# Дано число клеток
# Найти такое k, что mag(k+1) > n и mag(k)<=n
k_min = 0
k_max = 2000000
while(k_max - k_min > 1):
    kp = (k_min + k_max) // 2
    m = mag(kp)
    if(m>n):
        k_max = kp
    else:
        k_min = kp
print(k_min)
    
# print(mag(888888))