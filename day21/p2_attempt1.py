def split(p1_pos, p2_pos, p1_points, p2_points, turn, num_til_switch):
    if p1_points >= 21:
        return 1, 0
    if p2_points >= 21:
        return 0, 1

    if num_til_switch == 0:
        if turn:
            p1_pos = (p1_pos-1) % 10 + 1
            p1_points += p1_pos
        else:
            p2_pos = (p2_pos-1) % 10 + 1
            p2_points += p2_pos

        turn = not turn
        num_til_switch = 2

    if turn:
        s1 = split(p1_pos+1, p2_pos, p1_points,
                   p2_points, turn, num_til_switch-1)
        s2 = split(p1_pos+2, p2_pos, p1_points,
                   p2_points, turn, num_til_switch-1)
        s3 = split(p1_pos+3, p2_pos, p1_points,
                   p2_points, turn, num_til_switch-1)
    else:
        s1 = split(p1_pos, p2_pos+1, p1_points,
                   p2_points, turn, num_til_switch-1)
        s2 = split(p1_pos, p2_pos+2, p1_points,
                   p2_points, turn, num_til_switch-1)
        s3 = split(p1_pos, p2_pos+3, p1_points,
                   p2_points, turn, num_til_switch-1)

    p1_wins = s1[0] + s2[0] + s3[0]
    p2_wins = s1[1] + s2[1] + s3[1]

    print(p1_wins, p2_wins)

    return p1_wins, p2_wins


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t1) as f:
        lines = f.readlines()

    p1_pos = int(lines[0].replace('\n', ''))
    p2_pos = int(lines[1].replace('\n', ''))

    a = split(p1_pos, p2_pos, 0, 0, True, 2)
    print(a)


__main__()
