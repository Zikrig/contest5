input()
m = [int(i) for i in input().split()]

class Listwork:
    def __init__(self, m):
        self.m = m
        self.m.sort()
        # print(self.m)
        self.r = []
        self.get_all_zapr()
        # self.pos_first_a(5)
        # self.pos_first_a(1)
        # self.pos_first_a(2)
        # self.pos_first_a(9)

    def get_all_zapr(self):
        k = int(input())
        for kk in range(k):
            a, b = [int(i) for i in input().split()]
            # self.pos_first_a(a)
            self.r.append(self.zapr(a, b))
        print(*self.r)
        
    def zapr(self, a, b):
        first = self.m[0]
        fin = self.m[-1]

        if (a < first and b < first) or (a > fin and b > fin):
            return 0
        if (a < first and b > fin):
            return len(m)
        if (a < first):
            return self.pos_last_b(b)+1
        if (b > fin):
            return len(m) - self.pos_first_a(a)

        return self.pos_last_b(b)+1 - self.pos_first_a(a)
    
    def pos_first_a(self, a):
        # print(f'Ищем {a} в')
        # print(self.m)
        t1 = 0
        t2 = len(m)-1
        ts = -1
        while t2-t1>1:
            ts = (t1+t2) // 2
            # print(t1, t2, '->', ts)
            if(self.m[ts] >= a):
                t2 = ts
            else:
                t1 = ts
            # print(t1, t2, f'({self.m[t1]}, {self.m[t2]})')
        # print(t2, self.m[t2])
        if(m[t1] == a):
            return t1
        return t2
        
    
    def pos_last_b(self, b):
        # print(f'Ищем {b} в')
        # print(self.m)
        t1 = 0
        t2 = len(m)-1
        ts = -1
        while t2-t1>1:
            # print(t1, t2)
            ts = (t1+t2) // 2
            if(self.m[ts] > b):
                t2 = ts
            else:
                t1 = ts
        # print(t1, self.m[t1])
        if(m[t2] == b):
            return t2
        return t1

l = Listwork(m)