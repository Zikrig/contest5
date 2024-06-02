# import time

cnt = int(input())

def get_maybe_set(a, b):
    
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    

    r = [
        [
        (a[0] - dy, a[1] + dx),
        (b[0] - dy, b[1] + dx)
    ],
    [
        (a[0] + dy, a[1] - dx),
        (b[0] + dy, b[1] - dx)
    ]
    ]
    return r

def get_maybe_set_first(a, b):
    
    dx = b[0] - a[0]
    dy = b[1] - a[1]

    r = [
        (a[0] - dy, a[1] + dx),
        (b[0] - dy, b[1] + dx),
        (a[0] + dy, a[1] - dx),
        (b[0] + dy, b[1] - dx)
    ]
    return r

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
        s = dots[0]
        res = 1
        res_dots = set([
            (s[0]+1, s[1]),
            (s[0], s[1]+1),
            (s[0]+1, s[1]+1)
        ])
    
    # ttime = time.time()
    ldots = len(dots)
    for i in range(ldots):
        # if(i%100 == 0):
        #     print(time.time() - ttime)
            # ttime = time.time()
        for ii in range(i+1, ldots):
            a = dots[i]
            b = dots[ii]
            s = get_maybe_set_first(a, b)
            set_s = set(s)
            # print(set_s)
            r_item = set_s & dots_set
            # print(r_item)
            r_item -= set([a,b])
            # print(r_item)
            r = len(r_item)
            # print(r)

            if(res<2):
                res = 2
                res_dots = list(set_s-set([a,b]))[:2]

            # if r == 2:
            #     res = 4
            #     return []
            
            if r == 0:
                continue
            if(r == 1):
                res = 3
                res_dots = set(r_item)
                continue
            
            # print('222222222')
            sets_now = get_maybe_set(a, b)

            for s in sets_now:
                set_s = set(s)
                r_item = set_s & dots_set
                r_item -= set([a,b])
                r = len(r_item)
                if r == 2:
                    res = 4
                    return []
                    
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