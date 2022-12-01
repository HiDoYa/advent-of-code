def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

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

    num_steps = 10
    for _ in range(num_steps):
        new_state = ''
        for ind in range(len(state)-1):
            pair = state[ind] + state[ind+1]

            if pair in mapping:
                new_state += pair[0] + mapping[pair]
            else:
                new_state += pair[0]

            # Last loop
            if ind == len(state) - 2:
                new_state += pair[1]

        state = new_state

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

    count = counter[max_chr] - counter[min_chr]
    print(count)


__main__()
