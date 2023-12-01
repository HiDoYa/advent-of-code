line = File.open("test.txt").readlines.map(&:chomp)[0].split('')

line.each_with_index{|v,i|
    elements = line[i..i+13]
    if elements.uniq == elements
        p i + 14
        exit
    end
}
