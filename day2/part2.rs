use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::io::Error;

struct Instruction {
    direction: String,
    magnitude: i32,
}

fn get_instr(line: Result<String, Error>) -> Instruction {
    let lineval = line.expect("aaa 0");
    let split: Vec<&str> = lineval.split(" ").collect();
    let instr = Instruction {
        direction: split[0].to_string(),
        magnitude: split[1].parse::<i32>().unwrap(),
    };
    return instr;
}

fn main() {
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let instrs: Vec<Instruction> = buf.lines().map(get_instr).collect();

    let mut depth = 0;
    let mut horiz = 0;
    let mut aim = 0;

    for instr in instrs {
        match instr.direction.as_str() {
            "forward" => {
                horiz += instr.magnitude;
                depth += aim * instr.magnitude;
            }
            "down" => aim += instr.magnitude,
            "up" => aim -= instr.magnitude,
            _ => println!("Failed"),
        }
    }

    println!("Res: {}", depth * horiz)
}
