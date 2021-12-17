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
    pass


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    for line in lines:
        line_hex = line.replace('\n', '')

    version_total = 0

    ll = hex_to_bits(line_hex)
    bit_len = len(line_hex) * 4
    ll = ll.zfill(bit_len)

    while True:
        version_int, type_int, ll = read_header(ll)
        print("Version", version_int)
        print("Type", type_int)
        version_total += version_int

        if type_int == 4:
            literal_int, ll = read_literal(ll)
            print("Literal int", literal_int)
        else:
            length_type_id_bits = ll[0]
            ll = ll[1:]

            if length_type_id_bits == '0':
                length = bits_to_int(ll[:15])
                ll = ll[15:]
            elif length_type_id_bits == '1':
                num_subpackets = bits_to_int(ll[:11])
                ll = ll[11:]

        done = True
        for l in ll:
            if l != '0':
                done = False
                break

        if done or len(ll) == 0:
            break

    print(version_total)


__main__()
