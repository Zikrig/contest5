cnt = int(input())

def get_maybe_set(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]

    k1 = a[0] + dx/2 - dy/2
    if not is_round(k1):
        return[]
    k2 = a[1] + dy/2 + dx/2
    if not is_round(k2):
        return[]
    k3 = a[0] + dx/2 + dy/2
    if not is_round(k3):
        return[]
    k4 = a[1] + dy/2 - dx/2
    if not is_round(k4):
        return[]
    return [
        (round(k1), round(k2)),
        (round(k3), round(k4))
    ]
        

def is_round(some):
    r = round(some)
    if some == r:
        return True
    return False

def pre_check(s):
    mxvl = 1_000_000_000
    is_good = True
    for tu in s:
        for coord in tu:
            if(abs(coord) > mxvl):
                is_good = False
                break
    return is_good

def count_dots(dots):
    dots_set = set(dots)
    res = 0
    res_dots = set()

    if(len(dots_set)>0 and res == 0):
        for s in dots_set:
            res = 1
            res_dots = set([
                (s[0]+1, s[1]),
                (s[0], s[1]+1),
                (s[0]+1, s[1]+1)
            ])
            break
    
    for i in range(len(dots)):
        for ii in range(i+1, len(dots)):
            a = dots[i]
            b = dots[ii]
            s = get_maybe_set(a, b)
            if(s==[]):
                continue

            if(res<2):
                res = 2
                res_dots = set(s)

            set_s = set(s)
            r_item = (set_s & dots_set) - set([a,b])
            r = len(r_item)
            if r == 2:
                res = 4
                return []
            if r == 1:
                res = 3
                res_dots = set_s - r_item
                    
    return res_dots
            

dots = []
for i in range(cnt):
    dots.append(tuple(map(int, input().split())))

dots.sort()
# print(dots)
# dots.sort(key=lambda x:(x[0], x[1]))
# print(dots)
res = count_dots(dots)


print(len(res))
for t in res:
    print(*t)