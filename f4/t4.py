class Topic:
    def __init__(self, mass):
        self.mass = mass
        self.w = 0
        
        self.mrazdn = [0]
        for i in mass:
            self.mrazdn.append(self.mrazdn[-1]+i)

    def razn(self, a, b):
        # print(f"сумма от {self.mass[a]} до {self.mass[b]} будет {self.mrazdn[b+1]-self.mrazdn[a] + b-a}")
        return self.mrazdn[b+1]-self.mrazdn[a] + b-a
    
    def make_w(self, w):
        self.w = w
    # найти, какое максимальное число слов от 1 до w вместятся до конца строки
    def get_max_on(self, a):
        k1 = 0
        k2 = len(self.mrazdn)-a-1
        # print(f'Начиная с {a} можно вместить не более {k2} слов')
        while(k2-k1 > 1):
            ksr = (k2+k1)//2
            can_place = self.razn(a, a+ksr)
            if(can_place >= self.w):
                k2 = ksr
            else:
                k1 = ksr
        # print(f"{k1+1} слов можно вместить, начиная с {a+1}-того слова {self.mass[a]} длиной")
        return(k1+1)

    def place_text(self):
        cnt_of_strs = 0
        i = 0
        while i<len(self.mrazdn)-1:
            s_possible = self.get_max_on(i)
            cnt_of_strs += 1
            i+=s_possible
        return cnt_of_strs
            # print(f'{cnt_of_strs} я строчка вмещает {s_possible} слов')


w_comm_str, __, _ = input().split()
w_comm = int(w_comm_str)
mass1 = [int(i) for i in input().split()]
mass2 = [int(i) for i in input().split()]

t1 = Topic(mass1)
t2 = Topic(mass2)
split_dot_max = w_comm-max(mass2)+1
split_dot_min = max(mass1)-1
# print(f'поскольку w={w_comm} максимумы {max(mass1)},{max(mass2)}, точка разделения в ({split_dot_min},{split_dot_max})')
if(split_dot_max-split_dot_min > 1):
    while(split_dot_max-split_dot_min > 1):
        spl = (split_dot_min + split_dot_max)//2
        t1.make_w(spl)
        t2.make_w(w_comm-spl)
        r1 = t1.place_text()
        r2 = t2.place_text()
        if(r1>r2):
            split_dot_min = spl
            continue
        if(r2>r1):
            split_dot_max = spl
            continue
        break
    res = max(r1, r2)
else:
    spl = split_dot_min
    t1.make_w(spl)
    t2.make_w(w_comm-spl)
    r1 = t1.place_text()
    r2 = t2.place_text()

    rp = max(r1, r2)

    spl = split_dot_max
    t1.make_w(spl)
    t2.make_w(w_comm-spl)
    r1 = t1.place_text()
    r2 = t2.place_text()

    rp2 = max(r1, r2)

    res = min(rp, rp2)

    
print(res)
# print(f"При границе по {spl} в первом {r1}, во втором - {r2}")

# t1.place_text()
# t.get_max_on(6)
# t.get_max_on(2)