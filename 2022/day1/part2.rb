lines = File.open("input.txt").readlines.map(&:chomp)

current = 0
calories = []

for line in lines do
    if line.empty? then
        calories.append(current)
        current = 0
    else
        current += line.to_i
    end
end

calories = calories.sort
total = calories[-1] + calories[-2] + calories[-3]

p total
