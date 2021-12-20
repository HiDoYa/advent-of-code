PADDING = 4
ALTERNATE = '.'


def get_bin_at_px(image, cx, cy):
    if cx < 0 or cy < 0 or cx > len(image[0])-1 or cy > len(image)-1:
        return '1' if ALTERNATE == '#' else '0'

    if image[cy][cx] == '.':
        return '0'

    return '1'


def get_convol(image, cx, cy):
    bin = ''
    for y in range(cy-1, cy+2):
        for x in range(cx-1, cx+2):
            bin += get_bin_at_px(image, x, y)

    return int(bin, base=2)


def apply_convolv(image, enhancement):
    output_image = []

    for y in range(len(image)):
        output_image.append('')
        for x in range(len(image[0])):
            new_dat = enhancement[get_convol(image, x, y)]
            output_image[-1] += new_dat

    return output_image


def num_bright(image):
    bright = 0
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == '#':
                bright += 1
    return bright


def image_padding(image):
    lenx = len(image[0]) + PADDING*2
    top_padding = ALTERNATE * lenx
    left_padding = ALTERNATE * PADDING

    new_image = []
    for _ in range(PADDING):
        new_image.append(top_padding)

    for x in image:
        new_image.append(left_padding + x + left_padding)

    for _ in range(PADDING):
        new_image.append(top_padding)

    return new_image


def print_image(image):
    for y in range(len(image)):
        for x in range(len(image[0])):
            print(image[y][x], end='')
        print()
    print()


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    enhancement = lines[0].replace('\n', '')
    image = []
    for line in lines[2:]:
        line = line.replace('\n', '')
        image.append(line)

    global ALTERNATE
    for i in range(50):
        image = image_padding(image)
        image = apply_convolv(image, enhancement)
        ALTERNATE = '#' if ALTERNATE == '.' else '.'

    print(num_bright(image))


__main__()
