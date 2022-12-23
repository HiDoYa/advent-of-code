lines = File.open("input.txt").readlines.map(&:chomp)

def get_movement_dir(fm_coord, to_coord)
    x_dir = to_coord[0] <=> fm_coord[0]
    y_dir = to_coord[1] <=> fm_coord[1]
    [x_dir, y_dir]
end

def draw_on_map(coord, map, char, min_x)
    map[coord[1]][coord[0] - min_x] = char
end

def draw_from_to(fm_coord, to_coord, map, min_x)
    movement_dir = get_movement_dir(fm_coord, to_coord)
    current_coord = fm_coord

    while current_coord != to_coord
        draw_on_map(current_coord, map, "#", min_x)
        current_coord[0] += movement_dir[0]
        current_coord[1] += movement_dir[1]
    end

    draw_on_map(to_coord, map, "#", min_x)
end

def get_map_char(coord, map, min_x)
    map[coord[1]][coord[0] - min_x]
end

def sand_out_of_bounds(sand_current, min_x, max_x, floor)
    (
        sand_current[0] < min_x or
        sand_current[0] > max_x or
        sand_current[1] > floor
    )
end

def draw_floor(floor, min_x, max_x, map)
    fm_coord = [min_x, floor]
    to_coord = [max_x, floor]
    draw_from_to(fm_coord, to_coord, map, min_x)
end

def drop_sand(sand_source, map, min_x, max_x, floor)
    sand_current = sand_source
    moved = true

    below_rested = false
    left_below_rested = false
    rhgt_below_rested = false

    while moved
        moved = false
        below_rested = false
        left_below_rested = false
        rght_below_rested = false

        below_sand      = [sand_current[0]  , sand_current[1]+1]
        left_below_sand = [sand_current[0]-1, sand_current[1]+1]
        rght_below_sand = [sand_current[0]+1, sand_current[1]+1]

        if not sand_out_of_bounds(below_sand, min_x, max_x, floor)
            below_char = get_map_char(below_sand, map, min_x)
            if below_char == "."
                sand_current = below_sand
                moved = true
            elsif below_char == "#" or below_char == "o"
                below_rested = true
            end
        end

        if not sand_out_of_bounds(left_below_sand, min_x, max_x, floor) and not moved
            left_below_char = get_map_char(left_below_sand, map, min_x)
            if left_below_char == "."
                sand_current = left_below_sand
                moved = true
            elsif left_below_char == "#" or left_below_char == "o"
                left_below_rested = true
            end
        end

        if not sand_out_of_bounds(rght_below_sand, min_x, max_x, floor) and not moved
            rght_below_char = get_map_char(rght_below_sand, map, min_x)
            if rght_below_char == "."
                sand_current = rght_below_sand
                moved = true
            elsif rght_below_char == "#" or rght_below_char == "o"
                rght_below_rested = true
            end
        end
    end

    draw_on_map(sand_current, map, "o", min_x)
    (below_rested and left_below_rested and rght_below_rested)
end

# Find smallest X and largest Y
min_x = Float::INFINITY
max_x = 0
max_y = 0

lines.each do |line|
    line.split("->").map(&:strip).each do |pair|
        tok = pair.strip().split(",").map(&:to_i)
        min_x = [min_x, tok[0]].min
        max_x = [max_x, tok[0]].max
        max_y = [max_y, tok[1]].max
    end
end

# Arbitrary magic numbers (from guess and check)
min_x -= 320
max_x += 300

floor = max_y + 2

sand_source = [500, 0]

width = max_x - min_x + 1
height = floor + 1

map = Array.new(height) {Array.new(width) { '.' }}

draw_floor(floor, min_x, max_x, map)

lines.each do |line|
    clean_line = line.split("->").map(&:strip)
    num_coords = clean_line.length

    (num_coords-1).times do |index|
        fm_coord = clean_line[index].split(",").map(&:to_i)
        to_coord = clean_line[index + 1].split(",").map(&:to_i)
        draw_from_to(fm_coord, to_coord, map, min_x)
    end
end

draw_on_map(sand_source, map, "+", min_x)

i = 0
while drop_sand(sand_source, map, min_x, max_x, floor)
    i += 1
    if get_map_char(sand_source, map, min_x) == "o"
        break
    end
end
p i

# map.each do |l|
#     p l.join(" ")
# end