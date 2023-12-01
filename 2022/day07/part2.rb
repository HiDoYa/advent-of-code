DISK_SPACE = 70000000 
MIN_UNUSED_SPACE = 30000000
MAX_USED_SPACE = DISK_SPACE - MIN_UNUSED_SPACE

class Directory
    attr_accessor :directories, :total_file_size
    attr_reader :up, :total_size

    def initialize(up=nil)
        @directories = {}
        @total_file_size = 0
        @total_size = 0

        @up = up
    end

    def add_dir(dirname)
        directories[dirname] = Directory.new(self)
    end
    
    def compute_total
        total = @total_file_size
        @directories.each do |k, v|
            total += v.compute_total
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

    def get_all_totals
        totals = [@total_size]
        @directories.each do |k, v|
            totals += v.get_all_totals
        end

        return totals
    end
end

lines = File.open("input.txt").readlines.map(&:chomp)

root = Directory.new
current = nil

i = 0
until i == lines.length
    lines[i] = lines[i].delete_prefix("$").strip

    if lines[i].start_with? "cd"
        lines[i] = lines[i].delete_prefix("cd").strip
        
        if lines[i] == "/" then current = root
        elsif lines[i] == ".." then current = current.up
        else current = current.directories[lines[i]]
        end

        i += 1
    elsif lines[i].start_with? "ls"
        i += 1
        until (i == lines.length) || lines[i].start_with?("$")
            if lines[i].start_with? "dir"
                lines[i] = lines[i].delete_prefix("dir").strip
                current.add_dir(lines[i])
            else
                current.total_file_size += lines[i].split(' ')[0].to_i
            end

            i += 1
        end
    end
end

root.compute_total
all_totals = root.get_all_totals.sort

all_totals.each do |dir_total|
    if root.total_size - dir_total <= MAX_USED_SPACE
        p dir_total
        exit
    end
end