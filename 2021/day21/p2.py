import copy


# Indices: [player turn][p1 points][p2 points][p1 state][p2 state]
def init(dims=31, states=10):
    states_ll = []
    for _ in range(states):
        new = []
        for _ in range(states):
            new.append([0, 0])
        states_ll.append(new)

    ll = []
    for _ in range(dims+1):
        new = []
        for _ in range(dims+1):
            new.append(copy.deepcopy(states_ll))
        ll.append(new)

    # Set init conditions
    for a in range(dims):
        for b in range(dims):
            for c in range(states):
                for d in range(states):
                    if a >= 21 and b >= 21:
                        continue

                    if a >= 21:
                        ll[a][b][c][d] = [1, 0]
                    if b >= 21:
                        ll[a][b][c][d] = [0, 1]

    return [copy.deepcopy(ll), copy.deepcopy(ll)]


def add_pairs(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])


def get_state(state, dice_roll):
    return (state + dice_roll) % 10


def solve():
    ll = init()

    for p1_points in range(20, -1, -1):
        for p2_points in range(20, -1, -1):
            for p1_state in range(10):
                for p2_state in range(10):

                    # DICE ROLLS
                    for d1 in range(1, 4):
                        for d2 in range(1, 4):
                            for d3 in range(1, 4):
                                dice_roll = d1+d2+d3

                                new_p1_state = get_state(p1_state, dice_roll)
                                new_p2_state = get_state(p2_state, dice_roll)

                                ll[0][p1_points][p2_points][p1_state][p2_state] = add_pairs(
                                    ll[0][p1_points][p2_points][p1_state][p2_state],
                                    ll[1][p1_points+new_p1_state+1][p2_points][new_p1_state][p2_state])

                                ll[1][p1_points][p2_points][p1_state][p2_state] = add_pairs(
                                    ll[1][p1_points][p2_points][p1_state][p2_state],
                                    ll[0][p1_points][p2_points+new_p2_state+1][p1_state][new_p2_state])
    return ll


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    p1_pos = int(lines[0].replace('\n', ''))
    p2_pos = int(lines[1].replace('\n', ''))

    ll = solve()

    print(ll[0][0][0][p1_pos-1][p2_pos-1])


__main__()
