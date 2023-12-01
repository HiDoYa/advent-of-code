def compute_sum (char)
    if char.ord < 'a'.ord then
        return (char.ord - 'A'.ord + 1) + 26
    end

    return char.ord - 'a'.ord + 1
end

lines = File.open("input.txt").readlines.map(&:chomp)

sum = 0

lines.each_slice(3) do |l1, l2, l3| 
    l1, l2, l3 = [l1, l2, l3].map{|x| x.split('').uniq.sort}
    l2_index, l3_index = 0, 0
    
    l1.each { |c1|
        is_done = false

        while
            c2 = l2[l2_index]
            c3 = l3[l3_index]

            if c1 == c2 && c2 == c3 then
                sum += compute_sum(c1)
                is_done = true
                break
            elsif c1 > c2 then
                l2_index += 1
            elsif c1 > c3 then
                l3_index += 1
            else
                # c2 > c1 || c3 > c1
                break
            end
        end

        break if is_done
    }
end

p sum
