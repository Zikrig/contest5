input()
ropes = [int(i) for i in input().split()]
s = sum(ropes)
m = max(ropes)
if(s-m < m):
    print(2*m - s)
else:
    print(s)