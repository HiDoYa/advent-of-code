require 'set'

MULTIPLIER = 4000000
MAX_XY = 4000000

lines = File.open("input.txt").readlines.map(&:chomp)

def beacon_frequency(coord)
    coord[0] * MULTIPLIER + coord[1]
end

def manhattan_dist(coord1, coord2)
    (coord1[0] - coord2[0]).abs + (coord1[1] - coord2[1]).abs
end

def x_pos_within_dist(coord, y_dist, man_dist)
    x_diffs = man_dist - y_dist
    ([0, coord[0]-x_diffs].max..[MAX_XY-1, coord[0]+x_diffs].min)
end

def overlap?(r1, r2)
    r1.begin <= r2.end && r2.begin <= r1.end 
end

def merge_intervals(r1, r2)
    [r1.begin, r2.begin].min..[r1.end, r2.end].max
end

def merge_x_ranges(x_ranges)
    merges_found = true

    while merges_found
        merges_found = false
        len = x_ranges.length

        for i in 0..len-2 do
            for j in i+1..len-1 do
                if overlap?(x_ranges[i], x_ranges[j])
                    merges_found = true
                    merged = merge_intervals(x_ranges[i], x_ranges[j])
                    x_ranges.delete_at(j)
                    x_ranges.delete_at(i)
                    x_ranges.append(merged)
                    break
                end
            end

            break if merges_found
        end
    end
end

coords = lines.
    map{|l| l.scan(/x=(-?\d*), y=(-?\d*)/).
    map{|c| c.map(&:to_i)}}.
    map{|sensor_coord, beacon_coord|
        man_dist = manhattan_dist(sensor_coord, beacon_coord)
        [sensor_coord, beacon_coord, man_dist]
    }

MAX_XY.times do |y|
    x_ranges = []

    coords.each do |sensor_coord, beacon_coord, man_dist|
        y_dist = (sensor_coord[1] - y).abs
        next if y_dist > man_dist

        x_ranges.append(x_pos_within_dist(sensor_coord, y_dist, man_dist))
    end

    merge_x_ranges(x_ranges)

    if x_ranges.length != 1
        x_positions = (0..MAX_XY-1).to_a
        x_ranges.each{|x| x_positions -= x.to_a}
        coord = [x_positions[0], y]
        p "y: #{y}"
        p "x: #{x_positions[0]}"
        p beacon_frequency(coord)
    end
end

