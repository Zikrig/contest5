class Row:
    def __init__(self):
        self.my_max = -1
        self.my_second = -1

    def update(self, my_max):
        if(my_max >= self.my_max):
            self.my_second = self.my_max
            self.my_max = my_max
        elif(my_max > self.my_second):
            self.my_second = my_max
        

class Dlist:
    def __init__(self, n, m):
        self.i_list = [Row() for i in range(n)]
        self.j_list = [Row() for j in range(m)]
        self.n = n
        self.m = m
        self.t = []
        self.absolute_max_coords = []
        self.the_min = 1000000000
        self.min_coords = []

        self.get_t()

    def get_t(self):
        self.t = ([[int(i) for i in input().split()] for j in range(n)])
        self.absolute_max = -1
        self.absolute_max_coords = []
        for i in range(n):
            for j in range(m):
                self.i_list[i].update(self.t[i][j])
                self.j_list[j].update(self.t[i][j])
                
                if(self.t[i][j] > self.absolute_max):
                    self.absolute_max_coords.append((i, j))

                if(self.t[i][j] > self.absolute_max):
                    self.absolute_max = self.t[i][j]
                    self.absolute_max_coords = [(i, j)]

    def get_max_exept(self, i, j):
        total_mx = 0
        for ii in range(self.n):
            if(ii == i):
                continue
            now_el = self.t[ii][j]
            mx = 0
            if(now_el == self.i_list[ii].my_max):
                mx = self.i_list[ii].my_second
            else:
                mx = self.i_list[ii].my_max
            
            total_mx = max(total_mx, mx)

        for jj in range(self.m):
            if(jj == j):
                continue
            now_el = self.t[i][jj]
            mx = 0
            if(now_el == self.j_list[jj].my_max):
                mx = self.j_list[jj].my_second
            else:
                mx = self.j_list[jj].my_max
            
            total_mx = max(total_mx, mx)
        
        # print(f"максимум по таблице кроме строки {i} столбца {j} - {total_mx}")
        return total_mx
            

    def get_best_from_coords(self):
        for coords in self.absolute_max_coords:
            coord_i = coords[0]
            coord_j = coords[1]

            for j in range(self.m):
                maybe_min = self.get_max_exept(coord_i, j)
                if(maybe_min < self.the_min):
                    self.the_min = maybe_min
                    self.min_coords = [coord_i, j]

            for i in range(self.n):
                maybe_min = self.get_max_exept(i, coord_j)
                if(maybe_min < self.the_min):
                    self.the_min = maybe_min
                    self.min_coords = [i, coord_j]
  

        

    
n, m = [int(i) for i in input().split()]

dlist = Dlist(n, m)
dlist.get_best_from_coords()


# print(dlist.the_min)
print(*[i+1 for i in dlist.min_coords])
# Обойти каждую ячейку.
# сформировать список максиммумов и вторых мест по каждой строке и столбцу
# создать функцию, которая позволит быстро максимум без конкретной строки и столбца