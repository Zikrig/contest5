sl = input().split()
sl.sort(key=len)

slf = set([s[0] for s in sl])
# print(slf)

tozam = input().split()

for zam_ind in range(len(tozam)):
    
    zam = tozam[zam_ind]
    lzam = len(zam)
    z = zam[0]
    lenz = 1
    if(not z in slf):
        continue
    for s in sl:
        lens = len(s)
        if(lens > len(zam)):
            break
        if(lens > lzam):
            continue
        if(lens>lenz):
            z = zam[:lens]
            lenz = len(z)

        if(s == z):
            tozam[zam_ind] = s
            break


print(*tozam)