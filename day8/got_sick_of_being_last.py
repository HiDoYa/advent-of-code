# 0: 7 segments
# 1: 2 segments
# 2: 6 segments
# 3: 5 segments
# 4: 4 segments
# 5: 6 segments (has 1 more overlapping with 4 than 2 does)
# 6: 7 segments (must overlap with 1)
# 7: 3 segments
# 8: 8 segments
# 9: 7 segments (must overlap with 5)

# 1: 2 segments
# 7: 3 segments
# 4: 4 segments
# 3: 5 segments (must overlap with 1)
# 5: 5 segments (has 1 more overlapping with 4 than 2 does)
# 2: 5 segments
# 9: 6 segments (must overlap with 5 & 7)
# 0: 6 segments (must overlap with 7)
# 6: 6 segments
# 8: 7 segments

def all_overlap(s1, s2):
    for s in s1:
        if s not in s2:
            return False
    return True


def three_overlap(s1, s2):
    overlap_count = 0
    for s in s1:
        if s in s2:
            overlap_count += 1
    return overlap_count == 3


def find_num_for_str(mapping, str):
    for i, m in enumerate(mapping):
        if m == str:
            return i


with open('input.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    line = line.replace('\n', '')
    a = line.split(' | ')
    str1 = a[0].split(' ')
    str2 = a[1].split(' ')

    str1 = sorted(str1, key=len)

    mapping = [0] * 10

    for str in str1:
        str = ''.join(sorted(str))
        if len(str) == 2:
            mapping[1] = str
        if len(str) == 3:
            mapping[7] = str
        if len(str) == 4:
            mapping[4] = str
        if len(str) == 5:
            if all_overlap(mapping[1], str):
                mapping[3] = str
            elif three_overlap(mapping[4], str):
                mapping[5] = str
                pass
            else:
                mapping[2] = str
        if len(str) == 6:
            if all_overlap(mapping[5], str) and all_overlap(mapping[7], str):
                mapping[9] = str
            elif all_overlap(mapping[7], str):
                mapping[0] = str
            else:
                mapping[6] = str
        if len(str) == 7:
            mapping[8] = str

    current_num = 0
    for str in str2:
        str = ''.join(sorted(str))
        num = find_num_for_str(mapping, str)
        current_num = current_num * 10 + num

    count += current_num

print(count)
