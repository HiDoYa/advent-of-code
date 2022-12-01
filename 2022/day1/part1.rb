lines = File.open("input.txt").readlines.map(&:chomp)

current = 0
max = 0

for line in lines do
    if line.empty? then
        max = [current, max].max
        current = 0
    else
        current += line.to_i
    end
end

max = [current, max].max

p max
