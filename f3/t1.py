cnt = int(input())
input()
set_main = set(input().split())

for i in range(cnt-1):
    input()
    set_main = set_main & set(input().split())

print(len(set_main))
res = list(set_main)
res.sort()
print(*res)
