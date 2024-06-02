# Получение Партий
# Хранение их в Каталоге
# Возможность сортировки по Номеру или по Высоте
# Получение доступного Объема для заданной высоты
# Получение наиболее выгодной партии
# Коррекция списка в соответствии с ответом

class Party:
    def __init__(self, num, mzda, h):
        self.num = num
        self.mzda = mzda
        self.h = h
        self.mx = -1

class Catalog:
    def __init__(self, cnt):
        self.cnt = cnt
        self.parties = []
        self.lesn = {}
        self.lesnV = {}
        self.hs = []
        for i in range(int(self.cnt)):
            h, mzda = [int(j) for j in input().split()]
            p = Party(i, mzda, h)
            self.parties.append(p)

    def sort_num(self):
        self.parties.sort(key=lambda x: x.num)

    def sort_h(self):
        self.parties.sort(key=lambda x: x.h)
        self.mx = self.parties[-1].h

    def print_cat(self):
        for c in self.parties:
            print(f"{c.h}, номер {c.num}")
        print()

    def get_lesn(self):
        self.sort_h()

        pred = -2
        for i in range(len(self.parties)):
            # Для каждой высоты получить их общее количество
            h_now = self.parties[i].h
            print(h_now)
            if(h_now == pred):
                self.lesn[h_now] += 1
            else:
                self.lesn[h_now] = 1
            pred = h_now
            print(self.lesn)

        self.hs = list(self.lesn.keys())
        prev = 0
        # j = 0
        # ln = len(self.hs)
        # self.lesnV[0] = ['dwn': 0, 'h':0, 'cnt':0]
        nxt = 0
        v = 0
        for i in range(len(self.hs)-2,-1, -1):
            # print(f'Количество {self.hs[i]} это {self.lesn[self.hs[i]]}')
            h_now = self.hs[i+1]-self.hs[i]
            nxt += self.lesn[self.hs[i+1]]
            v += h_now*nxt
            nv = {
                'w':        self.hs[i],
                'want':     nxt,
                'h':        h_now,
                'v':        v
                # 'cnt':  
            }
            # nv = self.lesn[self.hs[i]] - self.lesn[self.hs[i-1]]
            self.lesnV[i+1] = nv
        self.lesnV[0] = {
            'w':        0,
            'want': self.mx,
            'h': self.lesnV[1]['w'],
            'v': v+self.mx*self.lesnV[1]['w']
        }
        # for i in range(1, len(self.hs)):
        #     v+=self.lesnV[i-1]['h']*self.lesnV[i-1]['want']
        #     self.lesnV[i]['v'] = v

    def get_all_dops_by_h(self, h):
        i1 = 0
        i2 = len(self.lesnV)
        while i2-i1>1:
            im = (i1+i2) // 2
            now_l = self.lesnV[im]
            print(f"Больше ли {now_l['w']}+{h} чем mx {self.mx}")
            # Максимальная высота после добавления прямоугольников до нужного
            pre_h = now_l['w'] + h
            if(pre_h > self.mx):
                i1 = im
            else:
                i2 = im
        
        ob = self.lesnV[i1]
        pre_h = ob['w']+h
        print(f"Нужный прямоугольник для дополнения {h} стоит на высоте {ob['w']} и предоставляет {ob['want']*ob['h']} в дополнение к {pre_h}")
    #     h_now = self.lesnV[i][0]
    #     x = mx - self.lesnV[i][0]
    #     print(i, self.lesn[i])
    #     y = self.lesn[self.lesnV[i][0]]
    #     n = (x//(y+1)) + 1
    #     print(f'Чтобы из колонки {h_now} длиной догнать {mx} нужно прибавить {n}')
            


    def print_lesn(self):
        for h in self.lesn:
            for i in range(self.lesn[h]):
                print('#' * h)

        for h in self.lesnV:
            print(self.lesnV[h])

cnt = int(input())

cat = Catalog(cnt)
cat.print_cat()
cat.get_lesn()
cat.print_lesn()
cat.get_all_dops_by_h(2)
cat.get_all_dops_by_h(3)
cat.get_all_dops_by_h(8)
cat.get_all_dops_by_h(0)

# Задача
# из 7 7 4 3
# получить
##
##
##
###
####
####
####