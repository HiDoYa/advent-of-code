use std::cmp;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn adder(num: u128) -> u128 {
    let mut sum = 0;
    for x in 1..(num + 1) {
        sum += x;
    }

    return sum;
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

    let mut min = u128::MAX;

    for i in nums[0]..nums[nums.len() - 1] {
        let fuel = nums
            .iter()
            .map(|x| (*x - i as i32).abs() as u128)
            .fold(0, |acc, x| acc + adder(x));

        min = cmp::min(min, fuel);
    }
    println!("{}", min);
}
