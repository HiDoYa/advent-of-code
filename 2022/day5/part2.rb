lines = File.open("input.txt").readlines.map(&:chomp)

i = lines.index ""
labels = lines[i-1]
num_boxes = labels.split(" ").last.to_i
indices = (0..num_boxes-1).map{|i| i * 4 + 1}

init_state = lines[..i-2]
instrs = lines[i+1..]

vals = init_state.map{|line|
    indices.map{|i| line[i]}
}.reverse

stacked = (0..num_boxes-1).map{|i|
    vals.map{|level|
        next level[i] unless level[i] == " "
    }.compact
}

instrs_vals = instrs.map{|instr|
    a = /move (\d+) from (\d+) to (\d+)/.match(instr)
    # 1 indexed to 0 indexed
    next a[1].to_i,a[2].to_i-1,a[3].to_i-1
}

instrs_vals.each{|num_move, from_loc, to_loc|
    popped_vals = (1..num_move).map{
        stacked[from_loc].pop
    }

    popped_vals.reverse.each{ |val|
        stacked[to_loc].push(val)
    }
}

p stacked.map{|stack| stack[-1]}.join