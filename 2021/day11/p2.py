def inc_pos(oct_map, x, y, pos_flashed):
    if x < 0 or x >= 10 or y < 0 or y >= 10:
        return oct_map, pos_flashed

    if oct_map[y][x] == 9 and pos_flashed[y][x] == False:
        pos_flashed[y][x] = True
        oct_map[y][x] = 0
        oct_map, pos_flashed = inc_pos(oct_map, x-1, y-1, pos_flashed)
        oct_map, pos_flashed = inc_pos(oct_map, x-1, y, pos_flashed)
        oct_map, pos_flashed = inc_pos(oct_map, x-1, y+1, pos_flashed)
        oct_map, pos_flashed = inc_pos(oct_map, x, y-1, pos_flashed)
        # oct_map, pos_flashed = inc_pos(oct_map, x, y, pos_flashed)
        oct_map, pos_flashed = inc_pos(oct_map, x, y+1, pos_flashed)
        oct_map, pos_flashed = inc_pos(oct_map, x+1, y-1, pos_flashed)
        oct_map, pos_flashed = inc_pos(oct_map, x+1, y, pos_flashed)
        oct_map, pos_flashed = inc_pos(oct_map, x+1, y+1, pos_flashed)
    elif pos_flashed[y][x] == False:
        oct_map[y][x] += 1

    return oct_map, pos_flashed


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    steps = 100
    oct_map = []

    for line in lines:
        line = line.replace('\n', '')
        oct_map.append([])
        for char in line:
            oct_map[-1].append(int(char))

    step = 1
    while True:
        pos_flashed = []
        for i in range(len(oct_map)):
            pos_flashed.append([False] * len(oct_map[i]))

        for y in range(len(oct_map)):
            for x in range(len(oct_map[y])):
                oct_map, pos_flashed = inc_pos(oct_map, x, y, pos_flashed)

        one_dull = False
        for a1 in pos_flashed:
            for a2 in a1:
                if not a2:
                    one_dull = True
                    break

        if not one_dull:
            print(step)
            break

        step += 1


__main__()
