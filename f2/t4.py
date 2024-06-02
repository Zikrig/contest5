def maketable():
    return [[0 for b in range(1,9)]for a in range(1,9)]


count_of_cells = int(input())

table = maketable()

for i in range(count_of_cells):
    cell = input().split()
    table[int(cell[0])-1][ int(cell[1])-1] = 1


res = 0
for row_num in range(len(table)):
    row = table[row_num]
    for cell_item_num in range(len(row)):
        cell_item = row[cell_item_num]
        if(cell_item == 0):
            continue
        
        boards_count = 4
        coords = [[row_num+1, cell_item_num], [row_num-1, cell_item_num], [row_num, cell_item_num+1], [row_num, cell_item_num-1]]
        for coords_item in coords:
            if(coords_item[0] >= 0 and coords_item[0] <= 7 and coords_item[1] >= 0 and coords_item[1] <= 7):
                if(table[coords_item[0]][coords_item[1]] == 1):
                    boards_count -= 1

        # print(boards_count)
        res += boards_count

# print(table)
print(res)