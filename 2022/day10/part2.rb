lines = File.open("input.txt").readlines.map(&:chomp)

def get_pixel(screen, x, instrs)
    mod_x = (instrs-1) % 40

    if mod_x == 0
        screen.append([])
    end

    if get_sprite_pos(x).include?(mod_x) 
        screen[-1].append("#")
    else
        screen[-1].append(".")
    end
end

def get_sprite_pos(x)
    [x-1,x,x+1]
end

x = 1
instrs = 0
screen = []

lines.each do |line|
    instrs += 1
    get_pixel(screen, x, instrs)

    if line.start_with? "noop"
    elsif line.start_with? "addx"
        instrs += 1
        get_pixel(screen, x, instrs)

        x += line.split(" ")[1].to_i
    end
end

screen.each do |line|
    p line.join()
end