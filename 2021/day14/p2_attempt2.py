import copy


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


def count_freq(freqs, first_char, last_char):
    counter = {}
    for pair in freqs:
        for chr in pair:
            if chr not in counter:
                counter[chr] = 0
            counter[chr] += freqs[pair]

    counter[first_char] += 1
    counter[last_char] += 1

    # Every single character is double counted except for first and last char
    for x in counter:
        counter[x] = int(counter[x] / 2)

    max_chr = 'N'
    min_chr = 'N'
    for x in counter:
        if counter[x] < counter[min_chr]:
            min_chr = x
        if counter[x] > counter[max_chr]:
            max_chr = x

    min_chr_freq = counter[min_chr]
    max_chr_freq = counter[max_chr]

    return min_chr_freq, max_chr_freq


def pair_to_newpair(pair, mapping):
    if pair not in mapping:
        return [pair]

    pair1 = pair[0] + mapping[pair]
    pair2 = mapping[pair] + pair[1]
    return [pair1, pair2]


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    mapping, state = parse(lines)

    freqs = {}
    for ind in range(len(state) - 1):
        pair = state[ind] + state[ind+1]
        if pair not in freqs:
            freqs[pair] = 0
        freqs[pair] += 1

    count = 40
    for i in range(count):
        new_freqs = copy.deepcopy(freqs)
        for pair in freqs:
            if freqs[pair] == 0:
                continue

            newpairs = pair_to_newpair(pair, mapping)
            for newpair in newpairs:
                if newpair not in new_freqs:
                    new_freqs[newpair] = 0
                new_freqs[newpair] += freqs[pair]

            new_freqs[pair] -= freqs[pair]

        freqs = new_freqs

    min_chr_freq, max_chr_freq = count_freq(freqs, state[0], state[-1])
    count = max_chr_freq - min_chr_freq
    print("Count:", count)


__main__()
