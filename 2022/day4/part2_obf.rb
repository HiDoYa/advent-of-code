p File.open("input.txt").readlines.map(&:chomp).map{ |l| 
    l.split(',').map{|x| x.split('-').map(&:to_i)}
}.flatten(2).each_slice(4).map{ |a,b,c,d|
    (a <= c && b >= c) || (c <= a && d >= a) || (a <= d && b >= d) || (c <= b && d >= b) ? 1 : 0
}.sum