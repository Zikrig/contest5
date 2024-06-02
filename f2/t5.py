# Это решение состряпано на коленке и я им не горжусь
# Но эй, оно хотя бы работает
class Berry:
    def __init__(self, number, a, b, claster_num):
        self.number = number
        self.a = a
        self.b = b

        self.delt = a-b
        self.claster_num = claster_num

        if(self.delt > 0):
            self.reason = self.b
        else:
            self.reason = self.a


def print_berries(berry):
    print('berries:')
    if(type(berry) != list):
        berry_list = [berry]
    else:
        berry_list = berry
    for b in berry_list:
        print(f"b.number, +{b.a}, -{b.b}, ={b.delt}")

count_of_berry = int(input())

berries_first = []
berries_second = []

max_berry = Berry(-2, -1, -1, 0)
# max_berry_otr = Berry(-2, -1, -1, 0)
for i in range(1, count_of_berry+1):
    a, b = input().split()
    new_berry = Berry(i, int(a), int(b), 0)

    if(new_berry.delt <= 0):
        new_berry.claster_num = len(berries_second)
        berries_second.append(new_berry)
        # if new_berry.reason > max_berry_otr.reason:
        #     max_berry_otr = new_berry
    else:
        new_berry.claster_num = len(berries_first)
        berries_first.append(new_berry)
    # print(f'new_berry_reason = {new_berry.reason}')
    if new_berry.reason > max_berry.reason:
        max_berry = new_berry

# print_berries(berries_first)
# print_berries(berries_second)
# print(f'наибольшая из ягод имеет а {max_berry.a} и добавит{max_berry.reason}')
# print(f'максимальную выгоду принесет {max_berry.number}')
# print(max_berry_alt.delt)
# если max_berry во втором кластере
if(max_berry.delt <= 0):
    berries_second.pop(max_berry.claster_num)
else:
    berries_first.pop(max_berry.claster_num)


max_height = 0
for berry_item in berries_first:
    max_height += berry_item.delt
    # print(f"max_height {max_height}")

max_height += max_berry.a
# print(f"max_height {max_height}")
print(max_height)
res_list = []
for berry_item in berries_first:
    res_list.append(berry_item.number)

# print(res_list)
# print(max_berry.number)
res_list.append(max_berry.number)
for berry_item in berries_second:
    res_list.append(berry_item.number)

print(*res_list)