def get_val(vars, var):
    if var.isalpha():
        return vars[var]
    else:
        return int(var)


def instrs(a, b, c, vars, val):

    pass


def has_zero(val):
    if len(str(val)) != 14:
        return False

    return '0' in str(val)


def decrement_val(val):
    temp_val = int(val)
    temp_val -= 1
    while has_zero(temp_val):
        temp_val -= 1

    return str(temp_val)


def __main__():
    # t1 = 'test_input.txt'
    # t2 = 'input.txt'
    # with open(t2) as f:
    #     lines = f.read().splitlines()

    val = '9' * 14
    abc_trips = [
        (1, 11, 1),
        (1, 10, 10),
        (1, 13, 2),
        (26, -10, 5),
        (1, 11, 6),
        (1, 11, 0),
        (1, 12, 16),
        (26, -11, 12),
        (26, -7, 15),
        (1, 13, 7),
        (26, -13, 6),
        (26, 0, 5),
        (26, -11, 6),
        (26, 0, 15)]

    while True:
        print(val)
        w = 0
        x = 0
        y = 0
        z = 0

        for index, (a, b, c) in enumerate(abc_trips):
            if a == 1:
                w = int(val[index])
                z *= 26
                z += w+c
            else:
                w = int(val[index])
                x = int((z % 26) + b != w)
                z //= a
                z *= 25*x+1
                z += (w+c)*x

        if z == 0:
            print(val)
            break

        val = decrement_val(val)


__main__()
