lines = File.open("input.txt").readlines.map(&:chomp)

points = 0
outcome_points = {
    'X' => 0, # Loss
    'Y' => 3, # Draw
    'Z' => 6, # Win
}

for line in lines do
    points += outcome_points[line[2]]

    char_displacement = -(line[2].ord - 'Y'.ord)
    char = ((line[0].ord - 'A'.ord) - char_displacement) % 3
    points += char + 1
end

p points
