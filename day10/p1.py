def corrupted():
    pass


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    err = 0
    for line in lines:
        q = []
        for char in line:
            if char == '[':
                q.append(char)
            if char == '(':
                q.append(char)
            if char == '{':
                q.append(char)
            if char == '<':
                q.append(char)

            if char == ')':
                if q[-1] == '(':
                    q = q[:-1]
                else:
                    err += 3
                    break
            if char == ']':
                if q[-1] == '[':
                    q = q[:-1]
                else:
                    err += 57
                    break
            if char == '}':
                if q[-1] == '{':
                    q = q[:-1]
                else:
                    err += 1197
                    break
            if char == '>':
                if q[-1] == '<':
                    q = q[:-1]
                else:
                    err += 25137
                    break

    print(err)


__main__()
