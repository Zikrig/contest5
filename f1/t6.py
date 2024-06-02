def getZnak(ost1, ost2):
    if(ost1 == 1 and ost2 == 1):
        return 'x'
    return '+'

input()
l = input().split()

# k = int(l[0])
# res = ''
# newform = []
# for i in range(len(l)):
#     newform.append(int(l[i]) % 2)

# print(newform)

k = int(l[0])
res = ''
for i in range(len(l)-1):

    newZnak = getZnak(k % 2, int(l[i+1]) % 2)
    res += newZnak

    k = (k % 2 + int(l[i+1]) % 2) % 2 if newZnak == '+' else (k % 2 * int(l[i+1]) % 2) % 2

print(res)