# Для числа:
# добавить к общему результату
# число операций для достижения x
# при разрешенных операциях +1 +4 -1
# f(0) = 0
# f(1) = 1
# f(2) = 2
# f(3) = 2
# f(4) = 1
# f(4n) = n
# f(4n+1) = n+1
# f(4n+2) = n+2
# f(4n+3) = n+2

def get_count_for_number(b):
    ost = b % 4
    res = b // 4
    
    if ost == 0:
        return res
    
    if ost == 1:
        return res + 1
    
    return res + 2

count_of_numbers = int(input())
res = 0
for i in range(count_of_numbers):
    res += get_count_for_number(int(input()))

print(res)