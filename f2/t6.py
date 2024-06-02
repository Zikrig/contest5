
# v это запас хода
# одно смещение это v-=k
# число смещений это v//k
# изначально мы на нулевом делении

def check_this_v(v):
    return ((v-1) // k) % len(circle)

input()
circle = [int(i) for i in input().split()]
a, b, k = [int(i) for i in input().split()]


init_v = check_this_v(a)
max_gain = -1
for v in range(a, b+1, k):
    v_possible = check_this_v(v)

    if(init_v == v_possible and v != a):
        break

    if(circle[v_possible] > max_gain):
        max_gain = circle[v_possible]
    # print(f'для v {v} {v_possible} с выигрышем {circle[v_possible]}')

    v_possible *= -1
    if(circle[v_possible] > max_gain):
        max_gain = circle[v_possible]
    # print(f'для v {v} {v_possible} с выигрышем {circle[v_possible]}')
        
print(max_gain)