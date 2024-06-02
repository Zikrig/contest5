count_of_sets = int(input())
for i in range(count_of_sets):
    input()
    set_now = [int(i) for i in input().split()]

    pack_now_start = 0
    pack_now_len = 0
    pack_now_min = set_now[0]
    packs_lens = []

    for a in range(len(set_now)):
        if(set_now[a] <= pack_now_len or pack_now_len >= pack_now_min):
            packs_lens.append(pack_now_len)
            pack_now_start = a
            pack_now_len = 1
            pack_now_min = set_now[a]
        else:
            pack_now_len += 1
            pack_now_min = min(set_now[a], pack_now_min)

        if(a == len(set_now)-1):
            packs_lens.append(pack_now_len)

    print(len(packs_lens))
    print(*packs_lens)
