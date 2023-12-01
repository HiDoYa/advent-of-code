lines = File.open("input.txt").readlines.map(&:chomp)

points = 0
outcome_points = {
    0 => 3, # Draw
    1 => 0, # Loss
    2 => 6, # Win
}

for line in lines do
    points += (line[2].ord - 'X'.ord) + 1

    opponent = line[0].ord - 'A'.ord
    player = line[2].ord - 'X'.ord
    diff = (opponent - player) % 3

    points += outcome_points[diff]
end

p points


# 0 0 = draw
# diff 0
# 0 1 = lose
# diff -1 -> 2
# 0 2 = win
# diff -2 -> 1

# 1 0 = win
# diff 1
# 1 1 = draw
# diff 0
# 1 2 = lose
# diff -1 -> 2

# 2 0 = lose
# diff 2
# 2 1 = win
# diff 1
# 2 2 = draw
# diff 0