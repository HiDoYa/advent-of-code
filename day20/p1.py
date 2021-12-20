PADDING = 8


def get_bin_at_px(image, cx, cy):
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
    lenx = len(image[0])

    for y in range(1, len(image)-1):
        output_image.append('.')
        for x in range(1, len(image[0])-1):
            new_dat = enhancement[get_convol(image, x, y)]
            output_image[-1] += new_dat
        output_image[-1] += '.'

    return output_image


def num_bright(image):
    bright = 0
    for y in range(2, len(image)-2):
        for x in range(2, len(image[0])-2):
            if image[y][x] == '#':
                bright += 1
    return bright


def image_padding(image):
    lenx = len(image[0]) + PADDING*2
    top_padding = '.' * lenx
    left_padding = '.' * PADDING

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

    image = image_padding(image)

    image = apply_convolv(image, enhancement)
    image = apply_convolv(image, enhancement)

    print_image(image)
    print(num_bright(image))


__main__()
