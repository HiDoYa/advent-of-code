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
    let num_lines = lines.len();
    let mut counts: [u32; 12] = [0; 12];

    for line in lines {
        let mut chars = line.chars();

        for i in 0..12 {
            counts[i] += chars.nth(0).unwrap().to_digit(10).unwrap();
        }
    }

    let stringval_gamma: String = counts
        .iter()
        .map(|count| {
            if *count as f64 > (num_lines as f64 / 2.0) {
                '1'
            } else {
                '0'
            }
        })
        .collect();
    let stringval_epsilon: String = stringval_gamma
        .chars()
        .map(|chr| if chr == '1' { '0' } else { '1' })
        .collect();

    let intval_gamma = isize::from_str_radix(stringval_gamma.as_str(), 2).unwrap();
    let intval_epsilon = isize::from_str_radix(stringval_epsilon.as_str(), 2).unwrap();

    println!("Res: {:?}", intval_gamma * intval_epsilon);
}
