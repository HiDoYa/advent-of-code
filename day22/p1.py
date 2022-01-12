def get_cubes(coord):
    x_min = max(-50, coord[0][0])
    x_max = min(50, coord[0][1])

    y_min = max(-50, coord[1][0])
    y_max = min(50, coord[1][1])

    z_min = max(-50, coord[2][0])
    z_max = min(50, coord[2][1])

    cubes = set()
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            for z in range(z_min, z_max+1):
                cubes.add((x, y, z))

    return cubes


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t1) as f:
        lines = f.readlines()

    instrs = []
    # list of coords
    # coords is a list of coord
    # coord has 3 lists of ranges for x, y, z
    ll_coords = []

    for line in lines:
        line = line.replace('\n', '')
        tok = line.split(' ')
        instr = tok[0]
        coords_str = tok[1].split(',')

        coords = []
        for a in coords_str:
            coord_str = a.split('=')[1].split('..')
            coords.append([int(coord_str[0]), int(coord_str[1])])

        instrs.append(instr)
        ll_coords.append(coords)

    on_set = set()

    for i in range(len(instrs)):
        cubes = get_cubes(ll_coords[i])

        if instrs[i] == 'on':
            on_set = on_set.union(cubes)
        else:
            on_set = on_set.difference(cubes)

    print(len(on_set))


__main__()
