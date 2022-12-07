class Directory
    attr_accessor :directories, :file_size_num
    attr_reader :up

    def initialize(up=nil)
        @directories = {}
        @file_size_num = 0

        @total_size = 0

        @up = up
    end

    def add_dir(dirname)
        directories[dirname] = Directory.new(self)
    end
    
    def calc_total
        total = @file_size_num
        @directories.each do |k, v|
            total += v.calc_total
        end

        @total_size = total
    end

    def sum_under_100k
        total = @total_size <= 100000 ? @total_size : 0

        @directories.each do |k, v|
            total += v.sum_under_100k
        end

        return total
    end
end

lines = File.open("input.txt").readlines.map(&:chomp)

root = Directory.new
current = nil

i = 0
until i == lines.length
    if !lines[i].start_with? "$ "
        raise
    end

    lines[i] = lines[i].delete_prefix("$ ")

    if lines[i].start_with? "cd "
        lines[i] = lines[i].delete_prefix("cd ")
        
        if lines[i] == "/"
            current = root
        elsif lines[i] == ".."
            current = current.up
        else
            current = current.directories[lines[i]]
        end

        i+= 1
    elsif lines[i].start_with? "ls"
        i += 1
        until (i == lines.length) || lines[i].start_with?("$")
            if lines[i].start_with? "dir "
                lines[i] = lines[i].delete_prefix("dir ")
                current.add_dir(lines[i])
            else
                current.file_size_num += lines[i].split(' ')[0].to_i
            end

            i += 1
        end
    end
end

root.calc_total
p root.sum_under_100k