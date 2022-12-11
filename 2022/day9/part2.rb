class RopePos
    def initialize()
        @x = 0
        @y = 0
    end

    attr_accessor :x, :y

    def is_touching(other)
        diff_x = (self.x - other.x).abs
        diff_y = (self.y - other.y).abs
        diff_x < 2 && diff_y < 2
    end

    def is_not_touching(other)
        !self.is_touching(other)
    end

    def move_self_towards(other)
        diff_x, diff_y = 0, 0 

        if self.y == other.y
            diff_x = unit(other.x - self.x)
        elsif self.x == other.x
            diff_y = unit(other.y - self.y)
        else
            diff_x = unit(other.x - self.x)
            diff_y = unit(other.y - self.y)
        end

        self.x += diff_x
        self.y += diff_y
    end
end

def unit(num)
    num < 0 ? -1 : 1
end

lines = File.open("input.txt").readlines.map(&:chomp).map{|x| x.split(' ')}.map{|x,y| [x, y.to_i]}

h_pos = RopePos.new
rope_pos = Array.new(9){RopePos.new}

visited = Hash.new
visited["0,0"] = true

lines.each do |dir, mag|
    mag.times do |i|
        # Move heads
        case dir
        when "R"
            h_pos.x += 1
        when "L"
            h_pos.x -= 1
        when "U"
            h_pos.y += 1
        when "D"
            h_pos.y -= 1
        end

        # Move tails
        ahead_rope_pos = h_pos
        rope_pos.each_with_index do |rope_pos, index|
            if ahead_rope_pos.is_not_touching(rope_pos)
                rope_pos.move_self_towards(ahead_rope_pos)

                if index == 8
                    visited["#{rope_pos.x},#{rope_pos.y}"] = true
                end
            end
            ahead_rope_pos = rope_pos
        end
    end
end

p visited.map{|x| x ? 1 : 0}.sum
