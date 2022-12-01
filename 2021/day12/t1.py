import copy


def traverse(current, mapping, level=0):
    if current == "end":
        return 1

    temp_mapping = copy.deepcopy(mapping)
    if current[0].islower():
        temp_mapping.pop(current)
        for x in temp_mapping:
            if current in temp_mapping[x]:
                temp_mapping[x].remove(current)

    count = 0
    for a in mapping[current]:
        temp_mapping_cur = copy.deepcopy(temp_mapping)

        count += traverse(a, temp_mapping_cur, level+1)

    return count


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    mapping = {"start": []}
    for line in lines:
        line = line.replace('\n', '')
        tok = line.split('-')
        if tok[0] not in mapping:
            mapping[tok[0]] = []
        if tok[1] not in mapping:
            mapping[tok[1]] = []

        mapping[tok[0]].append(tok[1])
        mapping[tok[1]].append(tok[0])

    count = traverse('start', mapping)

    print(count)


__main__()
