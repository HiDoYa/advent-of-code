import sys


def parse_file(lines):
    parse_2 = False

    dot_pos = []
    folds = []

    for line in lines:
        if line == '\n':
            parse_2 = True

        if not parse_2:
            line = line.replace('\n', '')
            tok = line.split(',')
            x = int(tok[0])
            y = int(tok[1])
            dot_pos.append((x, y))

        if parse_2:
            line = line.replace('\n', '')
            line = line.replace('fold along ', '')
            tok = line.split('=')
            chr = tok[0]
            if chr == 'x':
                folds.append(('x', int(tok[1])))
            if chr == 'y':
                folds.append(('y', int(tok[1])))

    return dot_pos, folds


def dims(dot_pos):
    x_max = 0
    y_max = 0
    for (x, y) in dot_pos:
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
    return (x_max, y_max)


def new_world(x, y):
    world = [[False for _ in range(y)] for _ in range(x)]
    return world


def get_world_dims(world):
    x_len = len(world)
    y_len = len(world[0])
    return x_len, y_len


def get_index(orig_x, orig_y, fold_dimension, fold_pos):
    new_x = orig_x
    new_y = orig_y
    lenx, leny = -1, -1

    if fold_dimension == 'x':
        if orig_x > fold_pos:
            # Constrain within current dims
            lenx = fold_pos
            new_x = orig_x - lenx

            # Flip
            new_x = lenx - new_x
    if fold_dimension == 'y':
        if orig_y > fold_pos:
            # Constrain within current dims
            leny = fold_pos
            new_y = orig_y - leny

            # Flip
            new_y = leny - new_y

    return new_x, new_y


def fold(world, dimension, pos):
    x_len, y_len = get_world_dims(world)
    if dimension == 'x':
        x_len = pos

    if dimension == 'y':
        y_len = pos

    world2 = new_world(x_len, y_len)

    for x in range(len(world)):
        if dimension == 'x' and pos == x:
            continue

        for y in range(len(world[0])):
            if dimension == 'y' and pos == y:
                continue

            newx, newy = get_index(x, y, dimension, pos)
            world2[newx][newy] = world2[newx][newy] or world[x][y]

    return world2


def print_world(world):
    x_max, y_max = get_world_dims(world)
    for y in range(y_max):
        for x in range(x_max):
            if world[x][y]:
                print('#', end='')
            else:
                print(' ', end='')
        print('')
    print('')


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    dot_pos, folds = parse_file(lines)

    x_max, y_max = dims(dot_pos)
    world = new_world(x_max+1, y_max+1)

    for (x, y) in dot_pos:
        world[x][y] = True

    for (dimension, pos) in folds:
        world = fold(world, dimension, pos)

    print_world(world)


__main__()
