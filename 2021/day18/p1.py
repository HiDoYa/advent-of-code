import ast
import math


def split(num):
    return [math.floor(num / 2), math.ceil(num / 2)]


def reduce_split(snail_fish_num):
    if isinstance(snail_fish_num, int):
        if snail_fish_num > 9:
            num = split(snail_fish_num)
            return True, num
        else:
            return False, snail_fish_num

    for i, ll in enumerate(snail_fish_num):
        reduced, new_ll = reduce_split(ll)
        if reduced:
            snail_fish_num[i] = new_ll
            return True, snail_fish_num
    return False, snail_fish_num


def find_pair(snail_fish_num, depth=1, num_accessed=0):
    if isinstance(snail_fish_num, int):
        return False, snail_fish_num, num_accessed + 1, None

    for i in range(len(snail_fish_num)):
        if depth >= 4 and isinstance(snail_fish_num[i], list):
            pair = snail_fish_num[i]
            snail_fish_num[i] = 0
            return True, snail_fish_num, num_accessed, pair

        reduced, snail_fish_num[i], num_accessed, pair = find_pair(
            snail_fish_num[i], depth+1, num_accessed)

        if reduced:
            return True, snail_fish_num, num_accessed, pair

    return False, snail_fish_num, num_accessed, None


def explode_pair(snail_fish_num, index, pair, depth=1, num_accessed=0):
    if isinstance(snail_fish_num, int):
        num_accessed += 1

        if num_accessed == index:
            snail_fish_num += pair[0]
            return False, snail_fish_num, num_accessed

        if num_accessed == index+2:
            snail_fish_num += pair[1]
            return True, snail_fish_num, num_accessed

        return False, snail_fish_num, num_accessed

    for i in range(len(snail_fish_num)):
        reduced, snail_fish_num[i], num_accessed = explode_pair(
            snail_fish_num[i], index, pair, depth+1, num_accessed)

        if reduced:
            return True, snail_fish_num, num_accessed

    return False, snail_fish_num, num_accessed


def reduce_pair(snail_fish_num):
    reduced, snail_fish_num, num_accessed, pair = find_pair(snail_fish_num)
    if reduced:
        _, snail_fish_num, _ = explode_pair(
            snail_fish_num, num_accessed, pair)

        return True, snail_fish_num

    return False, snail_fish_num


def add(n1, n2):
    current_snail_fish = [n1] + [n2]
    while True:
        reduced, current_snail_fish = reduce_pair(current_snail_fish)
        if reduced:
            continue

        reduced, current_snail_fish = reduce_split(current_snail_fish)
        if reduced:
            continue

        break

    return current_snail_fish


def magnitude(ll):
    if isinstance(ll, int):
        return ll

    return magnitude(ll[0]) * 3 + magnitude(ll[1]) * 2


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t1) as f:
        lines = f.readlines()

    snail_fish_nums = []
    for line in lines:
        line = line.replace('\n', '')
        snail_fish_num = ast.literal_eval(line)
        snail_fish_nums.append(snail_fish_num)

    current_snail_fish = snail_fish_nums[0]
    snail_fish_nums = snail_fish_nums[1:]

    for snail_fish in snail_fish_nums:
        current_snail_fish = add(current_snail_fish, snail_fish)

    print(current_snail_fish)
    print(magnitude(current_snail_fish))


__main__()
