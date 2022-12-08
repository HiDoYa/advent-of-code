lines = File.open("input.txt").readlines.map(&:chomp).map{|x| x.split('').map(&:to_i)}

width = lines[0].length
height = lines.length

visible_map = Array.new(height){Array.new(height, false)}

# Zero out left and right cols
(0..height-1).each do |y|
    x = 0
    visible_map[y][x] = true
    x = width - 1
    visible_map[y][x] = true
end

# Zero out top and bottom rows
(0..width-1).each do |x|
    y = 0
    visible_map[y][x] = true
    y = height - 1
    visible_map[y][x] = true
end


# Left to right (exclude edges)
(1..height-2).each do |y|
    max = lines[y][0]
    (1..width-2).each do |x|
        cur = lines[y][x]

        if cur > max
            visible_map[y][x] = true
        end

        max = [max, cur].max
    end
end

# Right to left (exclude edges)
(1..height-2).each do |y|
    max = lines[y][width-1]
    (1..width-2).reverse_each do |x|
        cur = lines[y][x]

        if cur > max
            visible_map[y][x] = true
        end

        max = [max, cur].max
    end
end

# Top to bottom (exclude edges)
(1..width-2).each do |x|
    max = lines[0][x]

    (1..height-2).each do |y|
        cur = lines[y][x]

        if cur > max
            visible_map[y][x] = true
        end

        max = [max, cur].max
    end
end

# Bottom to top (exclude edges)
(1..width-2).each do |x|
    max = lines[height-1][x]

    (1..height-2).reverse_each do |y|
        cur = lines[y][x]

        if cur > max
            visible_map[y][x] = true
        end

        max = [max, cur].max
    end
end

p visible_map.flatten.select{|x| x}.length