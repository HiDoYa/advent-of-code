lines = File.open("input.txt").readlines.map(&:chomp)

i = lines.index ""
num_boxes = lines[i-1].split(" ").last.to_i

stacked = (0..num_boxes-1).map{|x|
    lines[..i-2].map{|line|
        (0..num_boxes-1).map{|z| z * 4 + 1}.map{|x| line[x]}
    }.reverse.map{|level|
        next level[x] unless level[x] == " "
    }.compact
}

lines[i+1..].map{|instr|
    /move (\d+) from (\d+) to (\d+)/.match(instr)[1..3]
}.map{|x|x.map(&:to_i)
}.each{|num_move, from_loc, to_loc|
    (1..num_move).map{
        stacked[from_loc-1].pop
    }.reverse.each{ |val|
        stacked[to_loc-1].push(val)
    }
}

p stacked.map{|stack| stack[-1]}.join