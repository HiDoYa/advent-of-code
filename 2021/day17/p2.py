def is_inside(x, y, x_lo, x_hi, y_lo, y_hi):
    return y_lo <= y and y <= y_hi and x_lo <= x and x <= x_hi


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

    reached = 0

    # Found this number by trial and error
    # This is just brute force, don't copy this method
    magic_number = 400

    for init_x_vel in range(-magic_number, magic_number):
        for init_y_vel in range(-magic_number, magic_number):
            x_vel = init_x_vel
            y_vel = init_y_vel

            x, y = 0, 0
            while y > y_hi or (y >= y_lo and x_vel != 0 and not is_inside(x, y, x_lo, x_hi, y_lo, y_hi)):
                x += x_vel
                y += y_vel

                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1

                y_vel -= 1

            if is_inside(x, y, x_lo, x_hi, y_lo, y_hi):
                reached += 1

    print(reached)


__main__()
