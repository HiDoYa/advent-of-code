def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    line = lines[0]
    line.replace("target area: ", "")
    line.replace("\n", "")

    tok = line.split(', ')
    x_range = tok[0].split('=')[1].split('..')
    y_range = tok[1].split('=')[1].split('..')

    [x_lo, x_hi] = int(x_range[0]), int(x_range[1])
    [y_lo, y_hi] = int(y_range[0]), int(y_range[1])

    x, y = 0, 0

    x_vel, y_vel = 0, 0
    init_y_vel = 0

    total_max_y = 0
    delta_time = 0

    while True:
        init_y_vel += 1
        y_vel = init_y_vel

        max_y = 0
        y = 0

        while y > y_hi:
            max_y = max(y, max_y)
            y += y_vel
            y_vel -= 1

        if y_lo <= y and y <= y_hi:
            if max_y > total_max_y:
                total_max_y = max_y
                delta_time = 0
            else:
                delta_time += 1
        else:
            delta_time += 1

        # Terrible hack to stop after there are no updates
        # Do not ever copy this, this is not good
        if delta_time == 500:
            print(total_max_y)
            break


__main__()
