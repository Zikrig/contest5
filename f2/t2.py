n, k = [int(i) for i in input().split()]
days = [int(i) for i in input().split()]

# 5 4 2 1 9 4 2
#   $     % 

# На к дней вперед (или до конца, если до конца меньше к)
# мы должны знать максимальную цену
# тогда для дня d
# s(d) = max(s)
# k+=1
def make_storage(k):
    s = {}
    # к ВСЕГДА меньше len(days)
    for p_day in days[:k]:
        if(not p_day in s):
            s[p_day] = 1
        else:
            s[p_day] += 1
    return s

def max_not_zero(sl):
    mx = -100
    for k in list(sl.keys()):
        if(sl[k] <= 0):
            continue
        if(k>mx):
            mx = k
    return mx

if len(days) < k:
    max_r = 0
    for i in range(len(days)):
        t = max(days[i:])
        razn = t - days[i]
        if razn > max_r:
            max_r  = razn
else:
    max_r = 0
    for i in range(len(days)-1):
        if i+k<len(days):
            t = max(days[i:i+k+1])
        else:
            t = max(days[i:])
        # print(t)
        razn = t - days[i]
        if razn > max_r:
            max_r  = razn
    # s = make_storage(k)
    # max_r = 0
    # for i in range(len(days)-k):
    #     # print(s)
    #     # print(i)
    #     if(not days[i+k] in s):
    #         s[days[i+k]] = 1
    #     else:
    #         s[days[i+k]] += 1

    #     t = max_not_zero(s)
    #     razn = t - days[i]
    #     # print(t, days[i])
    #     if razn > max_r:
    #         max_r  = razn
        
    #     s[days[i]] -= 1
        

        

print(max_r)