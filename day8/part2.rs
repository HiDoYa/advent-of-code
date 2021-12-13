use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::iter::FromIterator;

fn read_input() -> Vec<String> {
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let lines: Vec<String> = buf.lines().map(|l| l.expect("")).collect();
    return lines;
}

fn all_overlap(s1: &String, s2: &String) -> bool {
    for s in s1.chars() {
        if !s2.contains(s) {
            return false;
        }
    }
    return true;
}

fn three_overlap(s1: &String, s2: &String) -> bool {
    let mut overlap_count = 0;
    for s in s1.chars() {
        if s2.contains(s) {
            overlap_count += 1
        }
    }
    return overlap_count == 3;
}

fn find_num_for_str(mapping: &Vec<String>, val: String) -> Option<i32> {
    for (i, m) in mapping.iter().enumerate() {
        if *m == val {
            return Some(i as i32);
        }
    }
    return None;
}

fn main() {
    let lines = read_input();

    let mut sum = 0;
    for line in lines {
        let inps: Vec<String> = line.split(" | ").map(|l| l.to_string()).collect();

        let mut num_strs: Vec<String> = inps[0].split(" ").map(|l| l.to_string()).collect();
        let key_strs: Vec<String> = inps[1].split(" ").map(|l| l.to_string()).collect();

        num_strs.sort_by_key(|l| l.len());

        let mut mapping: Vec<String> = vec!["".to_string(); 10];

        for num_str in num_strs {
            let mut chars: Vec<char> = num_str.chars().collect();
            chars.sort_by(|a, b| a.cmp(b));
            let s = String::from_iter(chars);

            match s.len() {
                2 => mapping[1] = s,
                3 => mapping[7] = s,
                4 => mapping[4] = s,
                5 => {
                    if all_overlap(&mapping[1], &s) {
                        mapping[3] = s;
                    } else if three_overlap(&mapping[4], &s) {
                        mapping[5] = s;
                    } else {
                        mapping[2] = s;
                    }
                }
                6 => {
                    if all_overlap(&mapping[5], &s) && all_overlap(&mapping[7], &s) {
                        mapping[9] = s;
                    } else if all_overlap(&mapping[7], &s) {
                        mapping[0] = s;
                    } else {
                        mapping[6] = s;
                    }
                }
                7 => mapping[8] = s,
                _ => panic!("Should not be here"),
            }
        }

        let mut current_num = 0;
        for key_str in key_strs {
            let mut chars: Vec<char> = key_str.chars().collect();
            chars.sort_by(|a, b| a.cmp(b));
            let s = String::from_iter(chars);

            let num = find_num_for_str(&mapping, s);
            current_num = current_num * 10 + num.unwrap();
        }

        sum += current_num;
    }
    println!("{:?}", sum);
}
