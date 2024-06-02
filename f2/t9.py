n = int(input())
t = [[int(j) for j in input().split()] for i in range(n)]
a = [k[0] for k in t]
b = [k[1] for k in t]
a.sort()
b.sort()
sr = b[n//2]

res = 0
for i in range(n):
    res += abs(a[i]-i-1)+abs(b[i]-sr)

print(res)

