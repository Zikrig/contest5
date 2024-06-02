class Catalog:
    def __init__(self):
        self.is_now_list = {}
        self.must_be = {}
        self.count_comm = 0

        self.swerka_res = {}
        self.res = 0

    def now_list_add(self, first, normal):
        n = str(normal[0])+'_'+str(normal[1])
        if(n in self.is_now_list):
            self.is_now_list[n].append(first)
        else:
            self.is_now_list[n] = [first]

    def must_be_list_add(self, first, normal):
        self.count_comm += 1
        n = str(normal[0])+'_'+str(normal[1])
        if(n in self.must_be):
            self.must_be[n].append(first)
        else:
            self.must_be[n] = [first]

    def swerka(self):
        for k in self.is_now_list:
            self.swerka_block(k)
        
        if (len(self.swerka_res) == 0):
            return self.count_comm
        else:
            return self.count_comm - max(self.swerka_res.values())

    def swerka_block(self, k):
        first = self.is_now_list[k]
        second = self.must_be[k]
        for f in first:
            for s in second:
                r1 = s[0]-f[0]
                r2 = s[1]-f[1]
                r_main = str(r1)+'_'+str(r2)
                if(r_main in self.swerka_res.keys()):
                    self.swerka_res[r_main] += 1
                else:
                    self.swerka_res[r_main] = 1
                    
    def optimize(self):
        set_now = set(self.is_now_list.keys())
        set_will = set(self.must_be.keys())
        set_and = set_now & set_will

        is_now_new = {}
        for n in self.is_now_list:
            if(n in set_and):
                is_now_new[n] = self.is_now_list[n]
            else:
                self.res += len(self.is_now_list[n])
        self.is_now_list = is_now_new

        must_be_new = {}
        for n in self.must_be:
            if(n in set_and):
                must_be_new[n] = self.must_be[n]
        self.must_be = must_be_new

    def print_all(self):
        for c in self.is_now_list:
            print(c)
        print()
        for c in self.must_be:
            print(c)

catalog = Catalog()
count_of_light = int(input())

for i in range(count_of_light):
    x1, y1, x2, y2 = [int(t) for t in input().split()]
    if(x1<x2):
        first = (x1,y1)
        second = (x2,y2)
    elif(x1>x2):
        first = (x2,y2)
        second = (x1,y1)
    elif(y1<y2):
        first = (x1,y1)
        second = (x2,y2)
    else:
        first = (x2,y2)
        second = (x1,y1)

    normal = (second[0]-first[0], second[1]-first[1])
    catalog.now_list_add(first, normal)

for i in range(count_of_light):
    x1, y1, x2, y2 = [int(t) for t in input().split()]
    if(x1<x2):
        first = (x1,y1)
        second = (x2,y2)
    elif(x1>x2):
        first = (x2,y2)
        second = (x1,y1)
    elif(y1<y2):
        first = (x1,y1)
        second = (x2,y2)
    else:
        first = (x2,y2)
        second = (x1,y1)

    normal = (second[0]-first[0], second[1]-first[1])
    catalog.must_be_list_add(first, normal)

catalog.optimize()
print(catalog.swerka())