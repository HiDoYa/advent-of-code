use std::cmp;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

#[derive(Debug)]
struct Instr {
    index: usize,
    instr: i32,
}
impl PartialEq for Instr {
    fn eq(&self, other: &Instr) -> bool {
        return self.instr == other.instr;
    }
}

fn opt_to_num(opt: Option<usize>, default: usize) -> usize {
    match opt {
        Some(x) => x,
        None => default,
    }
}

#[derive(Debug)]
struct Board {
    val: Vec<Vec<i32>>,
    marked: Vec<Vec<Option<usize>>>,
    num_steps: usize,
}
impl Board {
    fn mark(&mut self, instrs: &Vec<Instr>) {
        for (y, row) in self.val.iter().enumerate() {
            for (x, val) in row.iter().enumerate() {
                // Use binary search to see if this instruction exists
                let res = instrs.binary_search_by_key(val, |x| x.instr);
                match res {
                    Ok(vec_ind) => {
                        let index = instrs[vec_ind].index;
                        self.marked[y][x] = Some(index);
                    }
                    Err(_) => {}
                };
            }
        }
    }

    fn calc_num_steps(&mut self) {
        // Do a min through all dimensions to find num_steps
        let mut vert_min = usize::MAX;
        let mut horz_min = usize::MAX;
        for i in 0..5 {
            let mut cur_vert_min = usize::MIN;
            let mut cur_horz_min = usize::MIN;
            for j in 0..5 {
                cur_vert_min = cmp::max(opt_to_num(self.marked[j][i], usize::MIN), cur_vert_min);
                cur_horz_min = cmp::max(opt_to_num(self.marked[i][j], usize::MIN), cur_horz_min);
            }

            vert_min = cmp::min(cur_vert_min, vert_min);
            horz_min = cmp::min(cur_horz_min, horz_min);
        }

        self.num_steps = cmp::min(vert_min, horz_min);
    }

    fn get_last_instr_val(&self) -> Option<i32> {
        for y in 0..5 {
            for x in 0..5 {
                if opt_to_num(self.marked[y][x], usize::MAX) == self.num_steps {
                    return Some(self.val[y][x]);
                }
            }
        }
        return None;
    }

    fn calc_score(&self) -> i32 {
        let last_instr_val = self.get_last_instr_val().unwrap();

        let mut acc = 0;
        for y in 0..5 {
            for x in 0..5 {
                if opt_to_num(self.marked[y][x], usize::MAX) > self.num_steps {
                    acc += self.val[y][x];
                }
            }
        }

        return acc * last_instr_val;
    }
}

fn new_board() -> Board {
    Board {
        val: Vec::new(),
        marked: vec![vec![None; 5]; 5],
        num_steps: usize::MAX,
    }
}

fn read_input() -> Vec<String> {
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let lines: Vec<String> = buf.lines().map(|l| l.expect("")).collect();
    return lines;
}

fn parse_input(lines: Vec<String>) -> (Vec<i32>, Vec<Board>) {
    let mut lines_iter = lines.iter();
    let mut boards: Vec<Board> = Vec::new();

    let instrs_str = lines_iter.next();
    let instrs: Vec<i32> = instrs_str
        .unwrap()
        .split(',')
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    // Remove new line
    lines_iter.next();

    let mut current_board = new_board();
    for line in lines_iter {
        if line == "" {
            boards.push(current_board);
            current_board = new_board();
        } else {
            let board_nums: Vec<i32> = line
                .split(' ')
                .filter(|s| *s != "")
                .map(|s| s.parse::<i32>().unwrap())
                .collect();

            current_board.val.push(board_nums);
        }
    }

    boards.push(current_board);

    return (instrs, boards);
}

fn process_instrs(instrs_raw: Vec<i32>) -> Vec<Instr> {
    let mut instrs = instrs_raw
        .iter()
        .enumerate()
        .map(|(i, x)| Instr {
            instr: *x,
            index: i,
        })
        .collect::<Vec<Instr>>();

    instrs.sort_by_key(|x| x.instr);

    // Use PartialEq to remove duplicates
    instrs.dedup();

    return instrs;
}

fn main() {
    let lines = read_input();
    let (instrs_raw, mut boards) = parse_input(lines);
    let instrs = process_instrs(instrs_raw);

    for board in &mut boards {
        board.mark(&instrs);
        board.calc_num_steps();
    }

    boards.sort_by_key(|x| x.num_steps);

    let score = boards[0].calc_score();
    println!("{}", score);
}
