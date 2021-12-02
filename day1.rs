use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn main() {
    // Read lines
    let file = File::open("day1-input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let nums: Vec<i32> = buf.lines().map(|l| l.expect("0").parse::<i32>().unwrap()).collect();

    let mut increased = 0;
    for (i, num) in nums.iter().enumerate() {
        if i == 0 {
            continue;
        }

        if num > &nums[i-1] {
            increased += 1;
        }
    }

    println!("Increased: {}", increased)
}
