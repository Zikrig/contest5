import re

class Document:
    def __init__(self, w, h, c):
        self.w = w
        self.h = h
        self.c = c
        self.pics_actual = []
        self.cursor_x = 0
        self.cursor_y = 0
        self.final_pics_coords = []
        self.fragment = Fragment(0, self.w, self.h, self.c)

    def clear_pic(self, pic):
        args = re.findall(r"(\w+?)=([\w\-\d]+)", pic)
        args_list = {arg[0]:arg[1] for arg in args}
        
        if(args_list['layout'] == 'embedded'):
            pic = Picture_embedded(args_list['width'], args_list['height'], 'embedded')
            self.place_pic(pic)
            self.pics_actual.append(pic)

        if(args_list['layout'] == 'surrounded'):
            pic = Picture_surrounded(args_list['width'], args_list['height'], 'surrounded')
        
        if(args_list['layout'] == 'floating'):
            pic = Picture_floating(args_list['width'], args_list['height'], 'floating')
            pic.set_coords(args_list['dx'], args_list['dy'])

        return pic

    def parse_line(self, text_to_parse):
        abzac_pics = re.findall(r"\(image .*\)", text_to_parse)
        abzac = {}
        for i in range(len(abzac_pics)):
            abzac[i*2+1] = self.clear_pic(abzac_pics[i])

        abzac_text = re.split(r"\(image .*\)", text_to_parse)
        for i in range(len(abzac_text)):
            abzac[i*2] = abzac_text[i].split()

        return abzac

    def read_text(self):
        for line in lines[1:]:
            if(re.fullmatch(r"\s+", line)):
                self.make_actual_fragment()
            else:
                abzac = self.parse_line(line.replace('\n', ''))

                # print(abzac)
                for i in range(len(abzac)):
                    # print(i)
                    if(type(abzac[i]) == list):
                        for word in abzac[i]:
                            self.place_text(word)
                    else:
                        self.place_pic(abzac[i])
                    # print(abzac.keys())

    def place_text(self, word):
        res = self.try_to_place(self.cursor_x, len(word) * c)
        if(not res):
            self.make_actual_fragment()
            res = self.fragment.try_to_place(self.cursor_x, len(word) * c)
        print(res)
        pass

    def place_pic(self, pic):
        print(pic)
        if(pic.type_of_pic =='embedded'):
            res = self.fragment.try_to_place(self.cursor_x, pic.width)
            if(not res):
                self.make_actual_fragment()
                res = self.fragment.try_to_place(self.cursor_x, pic.width)

            print(res)
            pic.make_coords(res[0], res[1])
        # print(pic.type_of_pic)
        # функционал 
        pass

    def make_actual_fragment(self):
        self.cursor_x = 0
        
        # self.fragment = Fragment(self.cursor_y  + self.fragment.h, self.w, self.h)
        self.fragment.new_line()
        
        # ДОБАВИТЬ УДАЛЕНИЕ ЭЛЕМЕНТОВ ЗДЕСЬ
        # for pic in self.pics_actual:
        #     if(pic.y + pic.height <= self.fragment.y):
        #         self.pics_actual

        for pic in self.pics_actual:
            self.fragment.split_alittle(pic)
        

class Picture:
    def __init__(self, width, height, type_of_pic):
        self.width = int(width)
        self.height = int(height)
        self.type_of_pic = type_of_pic

class Picture_embedded(Picture):
    def make_coords(self, x, y):
        self.x = x
        self.y = y

class Picture_surrounded(Picture):
        pass

class Picture_floating(Picture):
    def set_coords(self, dx, dy):
        self.dx = dx
        self.dy = dy


# Если Фрагмент это новая строка, то перебираем актуальные картинки и делим его на фрагменты
class Fragment():
    def __init__(self, y, w, h, c):
        self.y = y
        self.w = w
        self.h_letter = h
        self.h = h
        self.c = c

        # хранит список
        # каждый элемент - список, начало и конец
        self.otr = [[0, self.w]]

    def embedded_h(self, h):
        if(h > self.h):
            self.h = h

    def split_alittle(self, pic):
        # даны промежутки типа 
        # 0 - 5, 40 - 120
        # Если у картинки y = 20 а width = 90, то новые промежутки
        # 0 - 5, 90 - 120

        # найти такой промежуток, что x1 или x2 внутри него
        # если x1, то заменить xp2 на него.
        # иначе заменить xp1 на него
        print(self.otr)
        

        for pr in range(len(self.otr)):
            if(self.otr[pr][0] < pic.x and self.otr[pr][1] > pic.x):
                self.otr[pr][1] = pic.x

            if(self.otr[pr][0] < pic.x + pic.width and self.otr[pr][1] > pic.x + pic.width):
                self.otr[pr][1] = pic.x + pic.width

    def new_line(self):
        self.y = self.y + self.h
        self.h = h

        self.otr = [[0, self.w]]

    def try_to_place(self, xmin, width):
        # найти такой отрезок, где xmin либо =x0, либо больше x0 и меньше x1. 
        # При этом x1-x2 должно быть не меньше с+width
        # слева направо, если отрезок не соответствует требованиям, то он приравнивается к [0:0]
        # Иначе ставим в отрезок и возвращаем координаты рисунка
        # если отрезка нет, то new_line

        for otr_item_i in range(len(self.otr)):
            otr_item = self.otr[otr_item_i]
            if otr_item == -1:
                continue
            if(otr_item[1]<=xmin):
                self.otr[otr_item_i] = -1
            
            if(otr_item[0] < xmin):
                self.otr[otr_item_i][0] = xmin

            if(self.otr[otr_item_i][1] - self.otr[otr_item_i][0] < width + self.c):
                self.otr[otr_item_i] = -1
            else:
                return self.otr[otr_item_i][0], self.y
                
        # не нашли места для рисунка
        return False
    

        




with open('input.txt', 'r') as file:
    lines = file.readlines()
# content = file.read()
# file.close()

w, h, c = [int(i) for i in lines[0].split()]

doc = Document(w, h, c)
doc.read_text()