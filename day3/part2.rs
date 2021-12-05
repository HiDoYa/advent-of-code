use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn read_input() -> Vec<String> {
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let lines: Vec<String> = buf.lines().map(|l| l.expect("")).collect();
    return lines;
}

fn get_most_common_bit(ll: &Vec<String>, current_bit_pos: usize) -> Option<char> {
    let mut num_0 = 0;
    let mut num_1 = 0;

    for line in ll {
        let chars: Vec<char> = line.chars().collect();
        let curr_char = chars[current_bit_pos];

        if curr_char == '0' {
            num_0 += 1;
        } else {
            num_1 += 1;
        }
    }

    if num_0 > num_1 {
        return Some('0');
    } else if num_1 > num_0 {
        return Some('1');
    }
    return None;
}

fn get_matching_nums(ll: &Vec<String>, chr: char, current_bit_pos: usize) -> Vec<String> {
    let mut num_list: Vec<String> = Vec::new();

    for line in ll {
        let chars: Vec<char> = line.chars().collect();
        let curr_char = chars[current_bit_pos];

        if curr_char == chr {
            num_list.push(line.to_string());
        }
    }
    return num_list;
}

fn get_result(ll: &Vec<String>) -> Option<isize> {
    if ll.len() == 1 {
        let res = isize::from_str_radix(ll[0].as_str(), 2).unwrap();
        return Some(res);
    }

    return None;
}

fn get_oxygen_rating(lines: &Vec<String>) -> i32 {
    let mut oxygen_rating: i32 = 0;
    let mut oxygen_list: Vec<String> = lines.clone();
    // Find oxygen rating
    for current_bit_pos in 0..12 {
        let mcb_res = get_most_common_bit(&oxygen_list, current_bit_pos);
        let mcb: char;
        match mcb_res {
            Some(x) => mcb = x,
            None => mcb = '1',
        }

        oxygen_list = get_matching_nums(&oxygen_list, mcb, current_bit_pos);

        let rating_res = get_result(&oxygen_list);
        match rating_res {
            Some(x) => {
                oxygen_rating = x as i32;
                break;
            }
            None => {}
        }
    }

    return oxygen_rating;
}

fn get_co2_rating(lines: &Vec<String>) -> i32 {
    let mut co2_rating: i32 = 0;
    let mut co2_list: Vec<String> = lines.clone();
    // Find co2 rating
    for current_bit_pos in 0..12 {
        let mcb_res = get_most_common_bit(&co2_list, current_bit_pos);
        let mcb: char;
        match mcb_res {
            Some(x) => mcb = x,
            None => mcb = '1',
        }
        let lcb = if mcb == '1' { '0' } else { '1' };

        co2_list = get_matching_nums(&co2_list, lcb, current_bit_pos);

        let rating_res = get_result(&co2_list);
        match rating_res {
            Some(x) => {
                co2_rating = x as i32;
                break;
            }
            None => {}
        }
    }

    return co2_rating;
}

fn main() {
    let lines = read_input();

    let oxygen_rating = get_oxygen_rating(&lines);
    let co2_rating = get_co2_rating(&lines);

    println!("Res: {:?}", oxygen_rating * co2_rating);
}
