# критерии
# Первая команда должна получить больше очков по результатам двух игр
# либо она должна получить больше очков в гостях и одинаково всего
# -если это возможно
# -если это требует меньше очков
def get_absolute_ost(g1,g2,f1,f2,p):
    first_count_or = g1 + f1 - g2 - f2
    first_count_home = g1-f2 if p == 2 else f1-g2

    # print(first_count_or)
    # print(first_count_home)
    if(g1 + f1 - g2 - f2 > 0):
        return 0
    
    f1 -= first_count_or
    first_count = g1 + f1 - g2 - f2
    first_count_home = g1-f2 if p == 2 else f1-g2
    # потенциальные изменения - голы нашей команды
    # По умолчанию считаем лучшим -first_count + 1
    # но готовы признать -first_count если first_count_guest - first_count > 0 и p = 2

    if(first_count_home > 0):
        # print(f"Разница в счете {first_count_or}")
        return first_count_or*(-1)

    # print(f"Разница в счете2 {-first_count_or+1}")
    return first_count_or * (-1)+1


g1, g2 = input().split(':')
f1, f2 = input().split(':')
p = input()

res = get_absolute_ost(
    int(g1),
    int(g2),
    int(f1),
    int(f2),
    int(p)
)
print(res)
# print(get_asbsolute_ost(0,0,0,0,1))