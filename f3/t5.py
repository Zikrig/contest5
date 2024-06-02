s = []
for i in range(3):
    input()
    s.append([int(i) for i in input().split()])


a = set(s[0]) & set(s[1])
b = set(s[1]) & set(s[2])
c = set(s[2]) & set(s[0])

res = list(a | b | c)
res.sort()
print(*res)