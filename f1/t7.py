class Game:
    def __init__(self, x, y, p, phi):
        self.days = 1
        self.x = int(x)
        self.y = int(y)
        self.p = int(p)
        self.t = 0
        self.game_on = True
        self.tower = True
        self.result = -1
        self.phi = phi

        self.game_goes()

    def check_tower(self):
        if(self.y <= 0):
            self.tower = False
        
    def up_t(self):
        if(not self.tower):
            return True

        self.t += self.p


    def check_absolute_end(self):
        if(self.y <=0 and self.t<= 0):
            self.result = self.days
            self.game_on = False
            return self.result
        
        if(self.x <=0):
            self.result = -1
            self.game_on = False
            return self.result

    def ordinary_move(self):
        delt = self.x - self.t
        if(delt <= 0):
            self.game_on = False
            pass

        self.t = 0
        self.y -= delt
        self.check_tower()

    def t_attacs(self):
        self.x -= self.t
        if(self.x <= 0):
            self.game_on = False

    def check_endgame(self):
        # Если мы готовы к эндгейму - то начинаем
        if((self.y + self.p) / self.x) < self.phi:
            return True
        return False
    
    def endgame_move(self):
        delt = self.y - self.x
        # Падение башни
        if(delt <= 0):
            self.y = 0
            self.t += delt
            self.tower = False
        else:
            self.y -= self.x

        if(self.t <= 0):
            self.game_on = False
            self.result = self.days
            return self.result
        
        self.t_attacs()

        if(self.x <= 0):
            self.game_on = False
            self.result = -1
            return self.result
        
        if(self.tower):
            self.up_t()

        self.days += 1
            

    
    def endgame_on(self):
        # print(f'day {self.days}, x:{self.x}, y: {self.y}, t:{self.t}')
        # При любом раскладе лучше бить ратушу
        while(self.game_on):
            # print(f'day {self.days}, x:{self.x}, y: {self.y}, t:{self.t} end ' + str(self.check_endgame()))
            self.endgame_move()
            self.check_absolute_end()

    def game_goes(self):
        while(self.game_on):
            if(self.check_endgame()):
                self.result = self.days
                self.endgame_on()
                break
            else:
                # обычная игра
                # Убить всех противников
                # print(f'day {self.days}, x:{self.x}, y: {self.y}, t:{self.t} end '+str(self.check_endgame()))
                self.ordinary_move()
                self.check_absolute_end()
                if(not self.game_on):
                    break

                self.t_attacs()
                if(not self.game_on):
                    break

                self.up_t()

                self.days +=1


x = input()
y = input()
p = input()

res = -1
for phi in range(1410, 1620, 1):
    game = Game(x, y, p, phi/1000)
    if(game.result != -1):
        if(game.result < res or res == -1):
            res = game.result

print(res)