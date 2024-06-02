countOfPairs = int(input())
amin, amax, bmin, bmax = 1000000000000, 0, 1000000000000, 0
for i in range(countOfPairs):
    aS, bS = input().split()
    a = int(aS)
    b = int(bS)
    
    if a < amin:
        amin = a
    if a > amax:
        amax = a

    if b < bmin:
        bmin = b
    if b > bmax:
        bmax = b

print(amin, bmin, amax, bmax)