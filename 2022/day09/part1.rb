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

visited = Hash.new
h_pos, t_pos = RopePos.new, RopePos.new
visited["#{t_pos.x},#{t_pos.y}"] = true

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
        if h_pos.is_not_touching(t_pos)
            t_pos.move_self_towards(h_pos)

            visited["#{t_pos.x},#{t_pos.y}"] = true
        end
    end
end

p visited.map{|x| x ? 1 : 0}.sum
