def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    p1_pos = int(lines[0].replace('\n', ''))
    p2_pos = int(lines[1].replace('\n', ''))

    p1_points = 0
    p2_points = 0

    num_rolls = 0
    current_dice = 1

    turn = True

    while p1_points < 1000 and p2_points < 1000:
        if turn:
            for _ in range(3):
                num_rolls += 1
                p1_pos += current_dice
                current_dice += 1
            p1_pos = (p1_pos-1) % 10 + 1
            p1_points += p1_pos
        else:
            for _ in range(3):
                num_rolls += 1
                p2_pos += current_dice
                current_dice += 1
            p2_pos = (p2_pos-1) % 10 + 1
            p2_points += p2_pos

        turn = not turn

    if p1_points >= 1000:
        print(p2_points * num_rolls)

    if p2_points >= 1000:
        print(p1_points * num_rolls)


__main__()
