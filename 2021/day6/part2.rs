use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

const NUMELEMENTS: usize = 7;

fn read_input() -> Vec<String> {
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let lines: Vec<String> = buf.lines().map(|l| l.expect("")).collect();
    return lines;
}

fn init_fish_buckets(line: String) -> Vec<u128> {
    let fishes: Vec<i32> = line.split(",").map(|x| x.parse::<i32>().unwrap()).collect();

    let mut fish_buckets: Vec<u128> = vec![0; NUMELEMENTS];
    for fish in fishes {
        fish_buckets[fish as usize] += 1;
    }

    return fish_buckets;
}

fn get_sum(fish_buckets: Vec<u128>) -> u128 {
    return fish_buckets.iter().fold(0, |acc, x| acc + x);
}

fn main() {
    let lines = read_input();

    let num_days = 256;
    let mut fish_buckets = init_fish_buckets(lines[0].clone());

    let mut new_elements = 0;
    let mut new_elements_old = 0;
    let mut new_elements_older;

    for day in 0..num_days {
        let i = day % NUMELEMENTS;

        new_elements_older = new_elements_old;
        new_elements_old = new_elements;
        new_elements = fish_buckets[i];

        fish_buckets[i] += new_elements_older;
    }

    let sum = get_sum(fish_buckets) + new_elements + new_elements_old;
    println!("{:?}", sum);
}
