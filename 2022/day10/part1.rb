lines = File.open("input.txt").readlines.map(&:chomp)

def print_if(sum, x, instrs)
    if [20, 60, 100, 140, 180, 220].include? instrs
        sum += x * instrs
        p "#{instrs}: #{x * instrs}"
    end
    sum
end

x = 1
sum = 0
instrs = 0

lines.each do |line|
    instrs += 1

    sum = print_if(sum, x, instrs)

    if line.start_with? "noop"
    elsif line.start_with? "addx"
        instrs += 1
        sum = print_if(sum, x, instrs)

        x += line.split(" ")[1].to_i
    end

end

p sum