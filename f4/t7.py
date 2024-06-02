class An:
    def __init__(self, n, m, k):
        self.n, self.m = n, m

        self.k = k
        self.ms = self.maxes_podr()

        self.get_razn_kv()

    def print_mass(self, m):
        for mm in m:
            print(*mm)

    def maxes_podr(self):
        res = []
        for i in range(len(self.k)):
            mx = -1
            mxnow = 0
            for j in range(len(self.k[0])):
                if k[i][j] == 1:
                    mxnow += 1
                    if(mxnow>mx):
                        mx = mxnow
                    # print(mx, mxnow)
                else:
                    mxnow = 0
            res.append(mx)
        return res
                

    def get_razn_kv(self):
        razn_lin = [[0 for i in range(self.m+1)]]
        for i in range(self.n):
            sm = 0
            # razn_lin.append([])
            newline = []
            for j in range(self.m):
                newline.append(sm)
                sm+=self.k[i][j]
            newline.append(sm)
            razn_lin.append(newline)

        self.razn_kv = []
        self.razn_kv.append([0 for i in range(self.m+1)])
        for i in range(self.n):

            newlen = [k for k in self.razn_kv[i]]
            for j in range(self.m+1):
                newlen[j] += razn_lin[i+1][j]
            # print(newlen)
        
            self.razn_kv.append(newlen)
    
    def try_spot(self, st, i, j):
        # Проверяет прямоугольник st*3st
        con = self.razn_kv[i+st*3][j+st] - self.razn_kv[i+st*3][j]
        nach = self.razn_kv[i][j+st] - self.razn_kv[i][j]

        resof = con - nach
        resgood = st*st*3
        # print(f"Для клетки {i} {j}: {resof} {resgood}")
        return con-nach == resgood
    
    def try_second(self, st, i, j):
        con = self.razn_kv[i+st*2][j+st*2]-self.razn_kv[i+st*2][j-st]
        nach = self.razn_kv[i+st][j+st*2]-self.razn_kv[i+st][j-st]
        # print(f"Для клетки {i} {j}: {con-nach}")
        return con-nach == st*st*3

    def try_all(self, st):
        icon = len(self.k)-st*3+1
        jnach = st
        jcon = len(self.k[0])-st*2+1

        if(icon <= 0 or jcon <=jnach):
            return False
        
        for i in range(icon):
            # Тут добавить проверку на то, что максимум строчки больше st и максимум строчки i+st больше st*3
            if self.ms[i] < st:
                continue
            if self.ms[i+st] < st:
                continue
            for j in range(jnach, jcon):
                # print(f"Проверяем {i} {j}")
                res_first_check = self.try_spot(st, i, j)
                if(res_first_check):
                    r = self.try_second(st, i, j)
                    if(r):
                        return True
        return False

    def try_binary(self):
        smax = min(self.n, self.m, max(self.ms)) // 3
        # print(f"smax {smax}")
        smin = 1
        while smax-smin > 1:
            spol = (smin+smax) // 2
            res = self.try_all(spol)
            if(res):
                smin = spol
            else:
                smax = spol
                
        if(self.try_all(smax)):
            return smax
        return smin

n, m = [int(i) for i in input().split()]
k  = []
for i in range(n):
    k.append([1 if a=='#' else 0 for a in input()])
an = An(n,m,k)


# an.print_mass(an.razn_kv)
# print(an.try_all(3))
print(an.try_binary())
# print(an.ms)