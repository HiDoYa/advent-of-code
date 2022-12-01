def get_val(vars, var):
    if var.isalpha():
        return vars[var]
    else:
        return int(var)


def alu(instr, val, vars, index):
    if "inp" in instr:
        a = instr.split()[1]

        # print(f'{a} = {val[index]}')
        vars[a] = int(val[index])
        index += 1

    elif "add" in instr:
        a = instr.split()[1]
        b = instr.split()[2]

        # print(f'{a} = {get_val(vars, a)} + {get_val(vars, b)}')
        vars[a] = get_val(vars, a) + get_val(vars, b)

    elif "mul" in instr:
        a = instr.split()[1]
        b = instr.split()[2]

        # print(f'{a} = {get_val(vars, a)} * {get_val(vars, b)}')
        vars[a] = get_val(vars, a) * get_val(vars, b)

    elif "div" in instr:
        a = instr.split()[1]
        b = instr.split()[2]

        # print(f'{a} = {get_val(vars, a)} / {get_val(vars, b)}')
        vars[a] = int(get_val(vars, a) / get_val(vars, b))

    elif "mod" in instr:
        a = instr.split()[1]
        b = instr.split()[2]

        # print(f'{a} = {get_val(vars, a)} % {get_val(vars, b)}')
        vars[a] = get_val(vars, a) % get_val(vars, b)

    elif "eql" in instr:
        a = instr.split()[1]
        b = instr.split()[2]

        # print(f'{a} = {get_val(vars, a)} == {get_val(vars, b)}')
        vars[a] = 1 if get_val(vars, a) == get_val(vars, b) else 0

    else:
        raise

    return vars, index


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
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.read().splitlines()

    val = '9' * 14
    while True:
        print(val)
        vars = {
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }
        index = 0

        for line in lines:
            # print(line, end=': ')
            vars, index = alu(line, val, vars, index)

        if vars['z'] == 0:
            print(val)
            break

        val = decrement_val(val)


__main__()
