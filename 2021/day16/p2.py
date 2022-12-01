import functools


def bits_to_int(x):
    return int(x, 2)


def hex_to_bits(x):
    return bin(int(x, 16))[2:]


def read_header(ll):
    version_bits = ll[:3]
    type_id_bits = ll[3:6]
    ll = ll[6:]

    version_int = bits_to_int(version_bits)
    type_int = bits_to_int(type_id_bits)

    return version_int, type_int, ll


def read_literal(ll):
    done = False
    bits = ''

    while not done:
        done = ll[0] == '0'
        ll = ll[1:]

        bits += ll[:4]
        ll = ll[4:]

    return bits_to_int(bits), ll


def parse_packet(ll):
    version_int, type_int, ll = read_header(ll)

    if type_int == 4:
        literal_int, ll = read_literal(ll)
        return literal_int, ll
    else:
        length_type_id_bits = ll[0]
        ll = ll[1:]

        num_list = []

        if length_type_id_bits == '0':
            length = bits_to_int(ll[:15])
            ll = ll[15:]

            target_length = len(ll) - length

            while len(ll) != target_length:
                # Get nums until length reached
                num_new, ll = parse_packet(ll)
                num_list.append(num_new)

        elif length_type_id_bits == '1':
            num_subpackets = bits_to_int(ll[:11])
            ll = ll[11:]

            for _ in range(num_subpackets):
                # Get nums until length reached
                num_new, ll = parse_packet(ll)
                num_list.append(num_new)

        if type_int == 0:
            # Sum
            num = functools.reduce(lambda a, b: a+b, num_list)
        if type_int == 1:
            # Product
            num = functools.reduce(lambda a, b: a*b, num_list)
        if type_int == 2:
            # Minimum
            num = functools.reduce(lambda a, b: a if a < b else b, num_list)
        if type_int == 3:
            # Maximum
            num = functools.reduce(lambda a, b: a if a > b else b, num_list)
        if type_int == 5:
            # Greater
            num = 1 if num_list[0] > num_list[1] else 0
        if type_int == 6:
            # Less
            num = 1 if num_list[0] < num_list[1] else 0
        if type_int == 7:
            # Equal to
            num = 1 if num_list[0] == num_list[1] else 0
    return num, ll


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    for line in lines:
        line_hex = line.replace('\n', '')

    ll = hex_to_bits(line_hex)
    bit_len = len(line_hex) * 4
    ll = ll.zfill(bit_len)

    num, ll = parse_packet(ll)

    print(num)


__main__()
