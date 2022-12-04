p File.open("input.txt").readlines.map(&:chomp)
.map{|x| x.split('').uniq.sort}.each_slice(3)
.map{|l1, l2, l3| (l1+l2+l3).sort}
.map{|b| b.select{|a| b.count(a) == 3}[0] }
.map{|c| c.ord < 'a'.ord ? (c.ord - 'A'.ord + 1) + 26 : c.ord - 'a'.ord + 1}.sum