# A solution I found on reddit that's a million times faster
# Very much black magic

instr, stack = [*open("input.txt")], []

p, q = 99999999999999, 11111111111111

for i in range(14):
    a = int(instr[18*i+5].split()[-1])
    b = int(instr[18*i+15].split()[-1])

    if a > 0:
        stack += [(i, b)]
        continue
    j, b = stack.pop()

    p -= abs((a+b)*10**(13-[i, j][a > -b]))
    q += abs((a+b)*10**(13-[i, j][a < -b]))

print(p, q)
