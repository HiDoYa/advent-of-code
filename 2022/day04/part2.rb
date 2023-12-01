lines = File.open("input.txt").readlines.map(&:chomp)


overlap = 0

lines.each do |line| 
    elf1, elf2 = line.split(',')
    elf1_range, elf2_range = [elf1, elf2].map{|x| x.split('-').map(&:to_i) }

    if elf1_range[0] <= elf2_range[0] && elf1_range[1] >= elf2_range[0] then
        overlap += 1
    elsif elf2_range[0] <= elf1_range[0] && elf2_range[1] >= elf1_range[0] then
        overlap += 1
    elsif elf1_range[0] <= elf2_range[1] && elf1_range[1] >= elf2_range[1] then
        overlap += 1
    elsif elf2_range[0] <= elf1_range[1] && elf2_range[1] >= elf1_range[1] then
        overlap += 1
    end
end

p overlap