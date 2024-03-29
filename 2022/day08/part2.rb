lines = File.open("input.txt").readlines.map(&:chomp).map{|x| x.split('').map(&:to_i)}

width = lines[0].length
height = lines.length

inner_height = (1..height-2)
inner_width = (1..width-2)

score = Array.new(height){Array.new(height, 1)}

def extract_score(bool_list)
    sum = 0
    bool_list.each do |v| 
        sum += 1
        if !v then break end
    end

    return sum
end

inner_height.each do |y|
    # Left to right (exclude edges)
    inner_width.each do |x|
        cur = lines[y][x]
        res = lines[y][..x-1].reverse.map{|val| val < cur}
        score[y][x] *= extract_score(res)
    end

    # Right to left (exclude edges)
    inner_width.reverse_each do |x|
        cur = lines[y][x]
        res = lines[y][x+1..].map{|val| val < cur}
        score[y][x] *= extract_score(res)
    end
end

inner_height.each do |x|
    # Top to bottom (exclude edges)
    inner_width.each do |y|
        cur = lines[y][x]
        res = lines[..y-1].map{|a| a[x]}.reverse.map{|val| val < cur}
        score[y][x] *= extract_score(res)
    end

    # Bottom to top (exclude edges)
    inner_width.reverse_each do |y|
        cur = lines[y][x]
        res = lines[y+1..].map{|a| a[x]}.map{|val| val < cur}
        score[y][x] *= extract_score(res)
    end
end

ans = (1..width-2).map do |x|
    (1..height-2).map do |y|
        score[y][x]
    end.max
end.max

p ans