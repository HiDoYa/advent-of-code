def str_mod_index(str, index, chr):
    temp_str = list(str)
    temp_str[index] = chr
    return "".join(temp_str)


def move_east_list(lines):
    can_move_east = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            next_col = col + 1
            if next_col == len(lines[row]):
                next_col = 0

            if lines[row][next_col] != '.':
                continue

            if lines[row][col] != '>':
                continue

            can_move_east.append((row, col))

    return can_move_east


def move_east(move_east, lines):
    for coords in move_east:
        row = coords[0]
        col = coords[1]

        next_col = col + 1
        if next_col == len(lines[row]):
            next_col = 0

        lines[row] = str_mod_index(lines[row], col, '.')
        lines[row] = str_mod_index(lines[row], next_col, '>')


def move_south_list(lines):
    can_move_south = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            next_row = row + 1
            if next_row == len(lines):
                next_row = 0

            if lines[next_row][col] != '.':
                continue

            if lines[row][col] != 'v':
                continue

            can_move_south.append((row, col))

    return can_move_south


def move_south(move_south, lines):
    for coords in move_south:
        row = coords[0]
        col = coords[1]

        next_row = row + 1
        if next_row == len(lines):
            next_row = 0

        lines[row] = str_mod_index(lines[row], col, '.')
        lines[next_row] = str_mod_index(lines[next_row], col, 'v')


def debug_lines(lines):
    for line in lines:
        print(line)
    print()


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.read().splitlines()

    step = 1
    while True:
        can_move_east = move_east_list(lines)
        move_east(can_move_east, lines)

        can_move_south = move_south_list(lines)
        move_south(can_move_south, lines)

        if not can_move_east and not can_move_south:
            break

        step += 1

    print(step)


__main__()
