import copy


def remove_state(temp_mapping, state):
    temp_mapping.pop(state)
    for x in temp_mapping:
        if state in temp_mapping[x]:
            temp_mapping[x].remove(state)
    return temp_mapping


def visited_twice(temp_states):
    for x in temp_states:
        if x == "start":
            continue
        if temp_states[x] == 2:
            return True
    return False


def traverse(current, mapping, states, add='', level=0):
    if current == "end":
        return 1

    temp_mapping = copy.deepcopy(mapping)
    temp_states = copy.deepcopy(states)

    if current[0].islower():
        if current not in temp_states:
            temp_states[current] = 0

        if visited_twice(temp_states) and temp_states[current] == 1:
            return 0

        if visited_twice(temp_states):
            temp_mapping = remove_state(temp_mapping, current)

        temp_states[current] += 1
        if temp_states[current] == 2:
            temp_mapping = remove_state(temp_mapping, current)

    count = 0
    for a in mapping[current]:
        count += traverse(a, temp_mapping,
                          temp_states, add+a, level+1)

    return count


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    mapping = {"start": []}
    states = {"start": 1}

    for line in lines:
        line = line.replace('\n', '')
        tok = line.split('-')
        if tok[0] not in mapping:
            mapping[tok[0]] = []
        if tok[1] not in mapping:
            mapping[tok[1]] = []

        mapping[tok[0]].append(tok[1])
        mapping[tok[1]].append(tok[0])

    count = traverse('start', mapping, states)

    print(count)


__main__()
