def corrupted():
    pass


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    incomplete_lines = []
    total_scores = []
    for line in lines:
        q = []
        corrupted = False
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
                if q[-1] != '(':
                    corrupted = True
                    break
                q = q[:-1]
            if char == ']':
                if q[-1] != '[':
                    corrupted = True
                    break
                q = q[:-1]
            if char == '}':
                if q[-1] != '{':
                    corrupted = True
                    break
                q = q[:-1]
            if char == '>':
                if q[-1] != '<':
                    corrupted = True
                    break
                q = q[:-1]

        if not corrupted:
            total_score = 0
            incomplete_lines.append(line)
            remaining_chars = []
            q.reverse()
            for char in q:
                if char == '[':
                    remaining_chars.append(']')
                    total_score *= 5
                    total_score += 2
                if char == '(':
                    remaining_chars.append(')')
                    total_score *= 5
                    total_score += 1
                if char == '{':
                    remaining_chars.append('}')
                    total_score *= 5
                    total_score += 3
                if char == '<':
                    remaining_chars.append('>')
                    total_score *= 5
                    total_score += 4

            total_scores.append(total_score)

    index = int((len(total_scores)-1)/2)
    print(sorted(total_scores)[index])


__main__()
