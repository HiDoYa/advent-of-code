def is_inside(coord1, coord2):
    # Coord1 is inside coord2
    x_min1 = coord1[0][0]
    x_max1 = coord1[0][1]
    y_min1 = coord1[1][0]
    y_max1 = coord1[1][1]
    z_min1 = coord1[2][0]
    z_max1 = coord1[2][1]

    x_min2 = coord2[0][0]
    x_max2 = coord2[0][1]
    y_min2 = coord2[1][0]
    y_max2 = coord2[1][1]
    z_min2 = coord2[2][0]
    z_max2 = coord2[2][1]

    return ((x_min1 >= x_min2 and x_max1 <= x_max2) and
            (y_min1 >= y_min2 and y_max1 <= y_max2) and
            (z_min1 >= z_min2 and z_max1 <= z_max2))


def is_partially_inside(coord1, coord2):
    x_min1 = coord1[0][0]
    x_max1 = coord1[0][1]
    y_min1 = coord1[1][0]
    y_max1 = coord1[1][1]
    z_min1 = coord1[2][0]
    z_max1 = coord1[2][1]

    x_min2 = coord2[0][0]
    x_max2 = coord2[0][1]
    y_min2 = coord2[1][0]
    y_max2 = coord2[1][1]
    z_min2 = coord2[2][0]
    z_max2 = coord2[2][1]

    cond1 = x_max1 < x_min2
    cond2 = x_max2 < x_min1
    cond3 = z_max1 < z_min2
    cond4 = z_max2 < z_min1
    cond5 = y_max1 < y_min2
    cond6 = y_max2 < y_min1

    return not cond1 and not cond2 and not cond3 and not cond4 and not cond5 and not cond6


def get_overlapping_region(coord1, coord2):
    x_min1 = coord1[0][0]
    x_max1 = coord1[0][1]
    y_min1 = coord1[1][0]
    y_max1 = coord1[1][1]
    z_min1 = coord1[2][0]
    z_max1 = coord1[2][1]

    x_min2 = coord2[0][0]
    x_max2 = coord2[0][1]
    y_min2 = coord2[1][0]
    y_max2 = coord2[1][1]
    z_min2 = coord2[2][0]
    z_max2 = coord2[2][1]

    pass


def get_area(coord):
    x_min = coord[0][0]
    x_max = coord[0][1]
    y_min = coord[1][0]
    y_max = coord[1][1]
    z_min = coord[2][0]
    z_max = coord[2][1]
    return (x_max - x_min) * (y_max - y_min) * (z_max - z_min)


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

    on_squares = []

    for i in range(len(instrs)):
        found = False
        on = instrs[i] == 'on'
        current_square = ll_coords[i]

        for sq_i, square in enumerate(on_squares):
            if on and is_inside(current_square, square):
                found = True
                on_squares[sq_i] = square
                break
            if on and is_inside(square, current_square):
                found = True
                on_squares[sq_i] = current_square
                break
            if not on and is_inside(square, current_square):
                found = True
                on_squares.pop(sq_i)
                break

            if is_partially_inside(current_square, square):
                found = True
                pass

        if not found and on:
            on_squares.append(current_square)

    area = 0
    for square in on_squares:
        area += get_area(square)

    print(area)


__main__()
