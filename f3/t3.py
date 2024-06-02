input()
digs = [int(i) for i in input().split()]
digs.sort()
if(len(set(digs))<2):
    print(0)
# elif(len(list(set(digs))) == len(digs)):
#     print(len(digs) - 1)
else:
    digsl = {}
    for i in range(0, len(digs)):
        if(digs[i] in digsl.keys()):
            digsl[digs[i]] += 1
        else:
            digsl[digs[i]] = 1

    finsp = list(set(digs))
    finsp.sort()
    # print(finsp)
    sl = {}
    for i in range(1, len(finsp)):
        if(abs(finsp[i-1]-finsp[i]) > 1):
            continue
        pr = str(finsp[i-1])+'_'+str(finsp[i])
        sl[pr] = digsl[finsp[i-1]] + digsl[finsp[i]]

    # print(sl)
    tomax = [sl[i] for i in sl]
    res = len(digs) - (max(tomax) if len(tomax) > 0 else 1)
    print(res)

