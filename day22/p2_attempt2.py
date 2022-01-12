class Cube:
    def __init__(self, x1, x2, y1, y2, z1, z2, on):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

        self.on = on

    def get_intersection(self, other):
        x1 = max(self.x1, other.x1)
        x2 = min(self.x2, other.x2)
        y1 = max(self.y1, other.y1)
        y2 = min(self.y2, other.y2)
        z1 = max(self.z1, other.z1)
        z2 = min(self.z2, other.z2)

        # No overlap
        if x1 > x2 or y1 > y2 or z1 > z2:
            return None

        intersection_state = other.on
        if self.on and other.on:
            intersection_state = False
        elif not self.on and not other.on:
            intersection_state = True

        return Cube(x1, x2, y1, y2, z1, z2, intersection_state)

    def volume(self):
        vol = (self.x2 - self.x1 + 1) * \
            (self.y2 - self.y1 + 1) * \
            (self.z2 - self.z1 + 1)

        if self.on:
            return vol
        return -vol


def parse_str(lines):
    cubes = []
    for line in lines:
        line = line.replace('\n', '')
        tok = line.split(' ')
        instr = tok[0]
        coords_str = tok[1].split(',')

        coords = []
        for a in coords_str:
            coord_str = a.split('=')[1].split('..')
            coords.append([int(coord_str[0]), int(coord_str[1])])

        on = instr == 'on'
        cubes.append(Cube(coords[0][0], coords[0][1], coords[1]
                     [0], coords[1][1], coords[2][0], coords[2][1], on))
    return cubes


def __main__():
    t1 = 'test_input.txt'
    t2 = 'input.txt'
    with open(t2) as f:
        lines = f.readlines()

    cubes = parse_str(lines)

    final_cube_list = []

    for cube in cubes:
        cube_to_add = []

        for final_cube in final_cube_list:
            intersection = final_cube.get_intersection(cube)
            if intersection is not None:
                cube_to_add.append(intersection)

        if cube.on:
            cube_to_add.append(cube)

        final_cube_list += cube_to_add

    total = 0
    for cube in final_cube_list:
        total += cube.volume()
    print(total)


__main__()
