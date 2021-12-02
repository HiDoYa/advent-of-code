use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn main() {
    // Read into lines
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let nums: Vec<i32> = buf.lines().map(|l| l.expect("0").parse::<i32>().unwrap()).collect();

    let mut increased = 0;
    for (i, num) in nums.iter().enumerate() {
        if i+3 > nums.len()-1 {
            break;
        }

        if num < &nums[i+3] {
            increased += 1;
        }
    }

    println!("Increased: {}", increased)
}