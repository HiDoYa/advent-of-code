import sys


def get_movements(x, y, x_max, y_max):
    indices = []
    if x != 0:
        indices.append((x-1, y))
    if y != 0:
        indices.append((x, y-1))
    if x != x_max:
        indices.append((x+1, y))
    if y != y_max:
        indices.append((x, y+1))
    return indices


def get_init_maps(lines):
    mapping = []
    cost = []
    for line in lines:
        line = line.replace('\n', '')
        cur_line_int = []
        for x in line:
            cur_line_int.append(int(x))

        mapping.append(cur_line_int)
        cost.append([sys.maxsize] * len(line))
    return mapping, cost


def debug(cost, x_max, y_max):
    for a in range(len(cost[0])):
        for b in range(len(cost)):
            val = cost[a][b]
            if val == sys.maxsize:
                print('--', end=' ')
            else:
                if val <= 9:
                    print(' ', end='')
                print(val, end=' ')
        print()
    print('\n')


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    mapping, cost = get_init_maps(lines)

    cur_x, cur_y = 0, 0
    cost[0][0] = 0
    x_max = len(mapping[0]) - 1
    y_max = len(mapping) - 1

    visited_nodes = []
    next_nodes = set()

    while True:
        # Reached end
        if cur_x == x_max and cur_y == y_max:
            print(cost[-1][-1])
            break

        visited_nodes.append((cur_x, cur_y))
        current = cost[cur_y][cur_x]
        indices = get_movements(cur_x, cur_y, x_max, y_max)

        # Calculate lowest cost
        for (next_x, next_y) in indices:
            if (next_x, next_y) in visited_nodes:
                continue

            next_val = current + mapping[next_y][next_x]
            cost[next_y][next_x] = min(cost[next_y][next_x], next_val)
            next_nodes.add((next_x, next_y))

        # Choose lowest cost path
        lowest_node, lowest_val = (-1, -1), sys.maxsize
        for (next_x, next_y) in next_nodes:
            if lowest_val >= cost[next_y][next_x]:
                lowest_val = cost[next_y][next_x]
                lowest_node = (next_x, next_y)

        next_nodes.discard(lowest_node)
        cur_x, cur_y = lowest_node[0], lowest_node[1]


__main__()
