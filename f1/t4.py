# Сохраняем список формул (по одной для координат каждой фигуры)
# перебор доски
# если поле не соответствует бою - плюсуем
class Chess:
    def __init__(self):
        self.chessbox = []
        self.void_count = 0
        self.input_chess()

        self.count_void()
        print(self.void_count)

        # self.pr()

    def input_chess(self):
        for i in range(8):
            self.chessbox.append(list(input())[:8])
        
        self.go_all()
            
            
    def go_all(self):
        for i in range(8):
            for j in range(8):
                self.spot_places(i,j)
    def spot_places(self, x, y):
        if(self.chessbox[x][y]=='R'):
            for i in range(x+1, 8):
                if(self.chessbox[i][y]) in ['R', 'B']:
                    break
                self.chessbox[i][y] = '#'
                
            for i in range(x-1, -1, -1):
                if(self.chessbox[i][y]) in ['R', 'B']:
                    break
                self.chessbox[i][y] = '#'

            for j in range(y+1,8):
                if(self.chessbox[x][j]) in ['R', 'B']:
                    break
                self.chessbox[x][j] = '#'
                
            for j in range(y-1, -1, -1):
                if(self.chessbox[x][j]) in ['R', 'B']:
                    break
                self.chessbox[x][j] = '#'

        if(self.chessbox[x][y]=='B'):
            i = x
            j = y
            while(i<7 and j<7):
                i+=1
                j+=1
                if(self.chessbox[i][j]) in ['R', 'B']:
                    break
                self.chessbox[i][j] = '#'
            i = x
            j = y  
            while(i<7 and j>0):
                i+=1
                j-=1
                if(self.chessbox[i][j]) in ['R', 'B']:
                    break
                self.chessbox[i][j] = '#'
            i = x
            j = y
            while(i>0 and j<7):
                i-=1
                j+=1
                if(self.chessbox[i][j]) in ['R', 'B']:
                    break
                self.chessbox[i][j] = '#'
            i = x
            j = y
            while(i>0 and j>0):
                i-=1
                j-=1
                if i == x and j == y:
                    continue
                if(self.chessbox[i][j]) in ['R', 'B']:
                    break
                self.chessbox[i][j] = '#'
                

    def count_void(self):
        for i in range(8):
            for j in range(8):
                # print(self.chessbox[i][j])
                if self.chessbox[i][j] == "*":
                    self.void_count +=1

    def pr(self):
        for r in self.chessbox:
            print(*r)

Chess()