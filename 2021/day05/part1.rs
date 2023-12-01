use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

#[derive(Debug, Copy, Clone)]
struct Coord {
    x: i32,
    y: i32,
}

impl Coord {
    fn get_between(&self, rhs: Coord) -> Vec<Coord> {
        let mut results: Vec<Coord> = Vec::new();

        if !(self.x == rhs.x || self.y == rhs.y) {
            return results;
        }

        let mut current = Coord {
            x: self.x,
            y: self.y,
        };

        results.push(current.clone());

        loop {
            if self.x > rhs.x {
                current.x -= 1;
            }
            if self.x < rhs.x {
                current.x += 1;
            }
            if self.y > rhs.y {
                current.y -= 1;
            }
            if self.y < rhs.y {
                current.y += 1;
            }

            results.push(current.clone());

            if current.x == rhs.x && current.y == rhs.y {
                break;
            }
        }

        return results;
    }
}

fn parse_coord(line: String) -> Coord {
    let vals: Vec<String> = line.as_str().split(',').map(|x| x.to_string()).collect();
    Coord {
        x: vals[0].parse::<i32>().unwrap(),
        y: vals[1].parse::<i32>().unwrap(),
    }
}

#[derive(Debug)]
struct Board {
    vals: Vec<Vec<i32>>,
}

impl Board {
    fn parse_line_str(&self, line: String) -> (Coord, Coord) {
        let result = str::replace(line.as_str(), " ->", "");
        let coords: Vec<String> = result.split(' ').map(|l| l.to_string()).collect();

        let c1 = parse_coord(coords[0].clone());
        let c2 = parse_coord(coords[1].clone());

        return (c1, c2);
    }

    fn draw_line(&mut self, line: String) {
        let (c1, c2) = self.parse_line_str(line);
        let points = c1.get_between(c2);

        for point in &points {
            self.vals[point.y as usize][point.x as usize] += 1;
        }
    }

    fn count_intersect(&self) -> i32 {
        let mut count = 0;
        for row in &self.vals {
            for val in row {
                if *val > 1 {
                    count += 1;
                }
            }
        }

        return count;
    }
}

fn new_board() -> Board {
    Board {
        vals: vec![vec![0; 1000]; 1000],
    }
}

fn read_input() -> Vec<String> {
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let lines: Vec<String> = buf.lines().map(|l| l.expect("")).collect();
    return lines;
}
fn main() {
    let lines = read_input();
    let mut board = new_board();

    for line in lines {
        board.draw_line(line.to_string());
    }

    let count = board.count_intersect();

    println!("{}", count);
}
