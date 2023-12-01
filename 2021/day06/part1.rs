use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn read_input() -> Vec<String> {
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let lines: Vec<String> = buf.lines().map(|l| l.expect("")).collect();
    return lines;
}
fn main() {
    let lines = read_input();
    let mut fishes: Vec<i32> = lines[0]
        .split(",")
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    let num_days = 80;

    for _ in 0..num_days {
        let mut num_new = 0;

        for fish in &mut fishes {
            *fish -= 1;

            if *fish == -1 {
                *fish = 6;
                num_new += 1;
            }
        }

        for _ in 0..num_new {
            fishes.push(8);
        }
    }

    println!("{}", fishes.len());
}
