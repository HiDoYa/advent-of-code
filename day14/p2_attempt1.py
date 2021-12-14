def parse(lines):
    mapping = {}
    state = ''

    for i, line in enumerate(lines):
        line = line.replace('\n', '')
        if i == 0:
            state = line
        elif i == 1:
            continue
        else:
            tok = line.split(' -> ')
            mapping[tok[0]] = tok[1]
    return mapping, state


def extrapolate(mapping, state):
    for x in mapping:
        mapping[x] = x[0] + mapping[x] + x[1]

    pairs = []
    for x in range(len(state) - 1):
        pairs.append(state[x] + state[x+1])

    new_mapping = {}
    for x in mapping:
        if x in pairs:
            new_mapping[x] = mapping[x]

    for i in range(40):
        for pair in new_mapping:
            val = new_mapping[pair]
            new_val = ''
            for ind in range(len(val)-1):
                temp_pair = val[ind] + val[ind+1]
                if temp_pair in mapping:
                    new_val += temp_pair[0] + mapping[temp_pair]
                else:
                    new_val += temp_pair[0]

                # Last loop
                if ind == len(val) - 2:
                    new_val += temp_pair[1]
            new_mapping[pair] = new_val
    return new_mapping


def count_freq(state):
    counter = {}
    for chr in state:
        if chr not in counter:
            counter[chr] = 0
        counter[chr] += 1

    max_chr = 'N'
    min_chr = 'N'
    for x in counter:
        if counter[x] < counter[min_chr]:
            min_chr = x
        if counter[x] > counter[max_chr]:
            max_chr = x

    min_chr_freq = counter[min_chr]
    max_chr_freq = counter[max_chr]

    return min_chr, max_chr, min_chr_freq, max_chr_freq


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    mapping, state = parse(lines)
    new_mapping = extrapolate(mapping, state)

    new_state = ''
    for x in range(len(state) - 1):
        pair = state[x] + state[x+1]
        if pair not in new_mapping:
            new_mapping[pair] = pair
        new_state += new_mapping[pair]

    _, _, min_chr_freq, max_chr_freq = count_freq(new_state)
    count = max_chr_freq - min_chr_freq
    print(count)


__main__()
