line = File.open("input.txt").readlines.map(&:chomp)[0].split('')

line.each_with_index{|v,i|
    elements = line[i..i+3]
    if elements.uniq == elements
        p i + 4
        exit
    end
}
