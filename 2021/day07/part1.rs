use std::cmp;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn factorial(num: u64) -> u64 {
    match num {
        0 => 1,
        1 => 1,
        _ => factorial(num - 1) * num,
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

    let mut nums: Vec<i32> = lines[0]
        .split(",")
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    nums.sort();

    let mut min = i32::MAX;
    for i in nums[0]..nums[nums.len() - 1] {
        let fuel = nums
            .iter()
            .map(|x| (*x - i as i32).abs())
            .fold(0, |acc, x| acc + x);

        min = cmp::min(min, fuel);
    }
    println!("{}", min);
}
