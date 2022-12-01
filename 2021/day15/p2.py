import sys
import copy


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


def add_to_map(mapping, adder):
    for a in range(len(mapping)):
        for b in range(len(mapping[0])):
            mapping[a][b] += adder
            if mapping[a][b] > 9:
                mapping[a][b] -= 9
    return mapping


def repeat_maps(mapping, cost):
    new_mapping = []
    new_cost = []

    for y in range(len(mapping)):
        new_list = []
        new_clist = []
        for i in range(5):
            new_list += list(map(lambda x: x+i if x+i <
                                 10 else x+i-9, mapping[y]))
            new_clist += cost[y]
        new_mapping.append(new_list)
        new_cost.append(new_clist)

    new_mapping2 = []
    new_cost2 = []
    for i in range(5):
        new_mapping2 += add_to_map(copy.deepcopy(new_mapping), i)
        new_cost2 += copy.deepcopy(new_cost)

    return new_mapping2, new_cost2


def debug(cost):
    for y in range(len(cost)):
        for x in range(len(cost[0])):
            val = cost[y][x]
            if val <= 9:
                print(end=' ')
            print(val, end=' ')
        print()
    print('\n')


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    mapping, cost = get_init_maps(lines)
    mapping, cost = repeat_maps(mapping, cost)

    cost[0][0] = 0
    y_max = len(mapping) - 1
    x_max = len(mapping[0]) - 1

    next_nodes = []
    next_nodes.append((0, 0))

    while next_nodes:
        (cur_x, cur_y) = next_nodes.pop(0)

        # Visit neighbor nodes
        indices = get_movements(cur_x, cur_y, x_max, y_max)

        # Calculate lowest cost
        for (next_x, next_y) in indices:
            next_val = cost[cur_y][cur_x] + mapping[next_y][next_x]
            curr_val = cost[next_y][next_x]

            if next_val < curr_val:
                cost[next_y][next_x] = next_val
                next_nodes.append((next_x, next_y))

    print(cost[-1][-1])


__main__()
