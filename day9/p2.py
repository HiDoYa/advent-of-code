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


def val_of_index(index, lines):
    return int(lines[index[1]][index[0]])


def main():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    seen_index = []

    basin_sizes = []

    for y in range(len(lines)):
        line = lines[y].replace('\n', '')

        for x in range(len(line)):
            char = line[x]
            cur_int = int(char)

            if (x, y) in seen_index:
                continue
            if cur_int == 9:
                seen_index.append((x, y))
                continue

            indices = indices_of_adjacent(x, y, len(line), len(lines))
            current_basin = 0

            for index in indices:
                if index in seen_index:
                    continue
                if val_of_index(index, lines) == 9:
                    seen_index.append(index)
                    continue

                seen_index.append(index)
                current_basin += 1

                indices += indices_of_adjacent(
                    index[0], index[1], len(line), len(lines))

            basin_sizes.append(current_basin)

    a = sorted(basin_sizes)
    print(a)
    print(a[-1] * a[-2] * a[-3])


main()
