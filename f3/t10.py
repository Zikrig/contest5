n, k = [int(i) for i in input().split()]


class Device:
    def __init__(self, k, n, num):
        self.n = n
        self.k = k
        self.num = num
        self.requests_now = {}
        self.pay_respect_to = ''
        if(num == 0):
            self.get_from = [0 for kk in range(k)]
        else:
            self.get_from = [-1 for kk in range(k)]

        self.significance = {nn:0 for nn in range(n)}
        self.significance.pop(self.num)
        self.res = -1
        self.mbres = -1
        self.i_have_not(self.mbres)

    def get_some(self, from_who, what):
        print(f"{from_who}->{self.num}: {what}")
        self.pay_respect_to = from_who
        
        self.get_from[what] = from_who
        self.i_have_not(self.mbres)

    def pay_respect(self):
        if(self.pay_respect_to != ''):
            self.significance[self.pay_respect_to] += 1
            self.pay_respect_to = ''

    def i_have_not(self, r):
        res = []
        for i in range(len(self.get_from)):
            if self.get_from[i] == -1:
                res.append(i)
        self.i_want = set(res)
        self.i_have = set([i for i in range(self.k)]) - self.i_want
        self.mbres = r
        if(len(self.i_want) == 0):
            if(self.res == -1):
                self.res = self.mbres
    
    def add_one(self, nn, kk):
        self.get_from[kk] = nn

    def request_of_part(self, what_want, who_want):
        self.requests_now[who_want] = what_want


class Catalog:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.cnt = -1
        self.l = [Device(k, n, i) for i in range(n)]
        self.get_rarest_part_min()

    def check(self):
        for ll in self.l:
            ll.i_have_not(self.cnt)
            if len(ll.i_want) > 0:
                return True
        return False
    
    def get_rarest_part_min(self):
        self.rarest = {i:0 for i in range(self.k)}
        # print('редкости')
        for ll in self.l:
            # ll.i_have_not(self.cnt)
            ll.mbres = self.cnt
            for k in ll.i_have:
                self.rarest[k] += 1
        self.rarest_not_all = list(map(lambda x: x[0], sorted(self.rarest.items(), key=lambda item: (item[1], item[0]))))
                
    def one_step(self, cnt):
        self.cnt = cnt
        # Получить приоритетный список
        self.get_rarest_part_min()

        # Что и у кого взять?
        for ll in self.l:
            if(len(ll.i_want) == 0):
                continue

            for w in self.rarest_not_all:
                if w in ll.i_want:
                    ll_want = w
                    break

            # sponsors = []
            i_have_min = 1000
            num_min = 1000
            sponsor_best = -1
            for ll_sponsore in self.l:
                if(ll_want in ll_sponsore.i_have):
                    if(len(ll_sponsore.i_have) == i_have_min):
                        if(ll_sponsore.num < num_min):
                            sponsor_best = ll_sponsore
                            num_min = sponsor_best.num
                    if(len(ll_sponsore.i_have) < i_have_min):
                        sponsor_best = ll_sponsore
                        i_have_min = len(sponsor_best.i_have)
                        num_min = sponsor_best.num
            
            sponsor_best.request_of_part(ll_want, ll.num)

        # Кому ответить?
        for ll in self.l:
            haver_max_significans = []
            max_significance = -1
            for ll_haver_num in ll.requests_now:
                ll_haver = self.l[ll_haver_num]
                if(ll.significance.get(ll_haver.num, -1) == max_significance):
                        haver_max_significans.append(ll_haver)
                if(ll.significance.get(ll_haver.num, -1) > max_significance):
                    max_significance = ll.significance[ll_haver.num]
                    haver_max_significans = [ll_haver]
            
            if(len(haver_max_significans) == 0):
                continue

            ll_best = haver_max_significans[0]
            for ll_haver in haver_max_significans:
                if(len(ll_haver.i_have) == len(ll_best.i_have)):
                    if(ll_haver.num < ll_best.num):
                        ll_best = ll_haver
                if(len(ll_haver.i_have) < len(ll_best.i_have)):
                    ll_best = ll_haver
            
            ll_best_num = ll_best.num
            self.l[ll_best_num].get_some(ll.num, ll.requests_now[ll_best_num])
            ll.requests_now = {}

        for ll in self.l:
            ll.pay_respect()

        if(len(self.rarest_not_all) == 0):
            return True
        return False
           

cat = Catalog(n, k)
c = False
l = 0
while(cat.check()):
    print(f"{l+1} ========================================================")
    cat.one_step(l)
    l+=1

print(*[ll.res+1 for ll in cat.l[1:]])