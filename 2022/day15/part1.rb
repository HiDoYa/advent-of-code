require 'set'

lines = File.open("input.txt").readlines.map(&:chomp)
# y = 10
y = 2000000

def manhattan_dist(coord1, coord2)
    (coord1[0] - coord2[0]).abs + (coord1[1] - coord2[1]).abs
end

def x_pos_within_dist(coord, y_dist, man_dist)
    x_diffs = man_dist - y_dist + 1

    ll = Set[coord[0]]
    x_diffs.times do |a|
        ll.add(coord[0] + a)
        ll.add(coord[0] - a)
    end

    ll
end

coords = lines.map{|l| l.scan(/x=(-?\d*), y=(-?\d*)/).map{|c| c.map(&:to_i)}}

x_positions = Set[]
coords.each do |sensor_coord, beacon_coord|
    man_dist = manhattan_dist(sensor_coord, beacon_coord)
    y_dist = (sensor_coord[1] - y).abs

    next if y_dist > man_dist

    x_positions_new = x_pos_within_dist(sensor_coord, y_dist, man_dist)
    x_positions.merge(x_positions_new)
end

coords.each do |s, b|
    x_positions.delete(b[0]) if b[1] == y
end

p x_positions.length
