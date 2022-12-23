heightmap = File.open("input.txt").readlines.map(&:chomp)

def get_height(heightmap, index)
    heightmap[index[0]][index[1]]
end

def get_distances(distances, index)
    distances[index[0]][index[1]]
end

def get_adjacent(indices, current, heightmap, visited, to_visit, height, width)
    vals = [
        [indices[0], indices[1] - 1],
        [indices[0], indices[1] + 1],
        [indices[0] - 1, indices[1]],
        [indices[0] + 1, indices[1]],
    ]


    vals.
        select{ |n| n[0] >= 0 and n[1] >= 0}.
        select{ |n| n[0] < height and n[1] < width}.
        select{ |n| not visited.include? n}.
        select{ |n| not to_visit.include? n}.
        select{ |n| get_height(heightmap, n).ord + 1 >= get_height(heightmap, current).ord }
end

start_indices = [0, 0]
s_indices = [0, 0]

height = heightmap.length
width = heightmap[0].length
distances = Array.new(height) { Array.new(width) { 0 } }

heightmap.each_with_index do |line, line_index|
    if line.include? "S"
        chr_index = line.split("").find_index("S")
        start_indices = [line_index, chr_index]
    end

    if line.include? "E"
        chr_index = line.split("").find_index("E")
        start_indices = [line_index, chr_index]
    end
end

heightmap[start_indices[0]][start_indices[1]] = 'z'
heightmap[s_indices[0]][s_indices[1]] = 'a'

distances[start_indices[0]][start_indices[1]] = 0
visited = []
to_visit = [start_indices]

while not to_visit.empty?
    p to_visit.length
    to_visit.sort_by{ |indices| get_distances(distances, indices) }

    # Get next node
    current = to_visit[0]
    to_visit = to_visit[1..]
    visited.append(current)

    current_height = get_height(heightmap, current)
    current_distance = get_distances(distances, current)

    if current_height == 'a'
        p "End found in #{current_distance}"
        break
    end

    adjs = get_adjacent(current, current, heightmap, visited, to_visit, height, width)

    adjs.each do |adj|
        distances[adj[0]][adj[1]] = current_distance + 1
    end

    to_visit += adjs
end