lines = File.open("input.txt").readlines.map(&:chomp)

sum = 0

for line in lines do
    part_len = line.length / 2

    comp_1 = line[0..part_len-1].split('')
    comp_2 = line[part_len..].split('')

    comp_1.each { |c1| 
        if comp_2.include? c1 then
            if c1.ord < 'a'.ord then
                sum += (c1.ord - 'A'.ord + 1) + 26
            else
                sum += (c1.ord - 'a'.ord + 1)
            end

            break
        end
    }
end

p sum