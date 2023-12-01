def risk_level(height):
    return height + 1


def indices_of_adjacent(x, y, lenx, leny):
    indices = []
    if x != 0:
        indices.append((x-1, y))
    if y != 0:
        indices.append((x, y-1))
    if x != lenx-1:
        indices.append((x+1, y))
    if y != leny-1:
        indices.append((x, y+1))

    return indices


def main():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    res = 0
    for y in range(len(lines)):
        line = lines[y].replace('\n', '')
        for x in range(len(line)):
            char = line[x]
            cur_int = int(char)

            indices = indices_of_adjacent(x, y, len(line), len(lines))
            is_lowest = True
            for (xnew, ynew) in indices:
                if cur_int >= int(lines[ynew][xnew]):
                    is_lowest = False
                    break

            if is_lowest:
                res += risk_level(int(line[x]))

    print(res)


main()
