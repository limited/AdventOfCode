pub fn part1() {
    println!("Day 3");
    let str = include_str!("day3_input");

    let len: u32 = str.lines().next().unwrap().len() as u32;
    println!("len: {}", len);
    let mut counts = vec![0; len.try_into().unwrap()];
    counts = str.lines().fold(counts, |acc, l| parse_line(acc, l));

    let total = str.lines().count() as u32;

    //println!("{:#?}", counts);

    let mut gamma = 0;
    let mut epsilon = 0;

    for (i, count) in counts.iter().enumerate() {
        println!("pos {} count of {}", i, count);
        let bit_idx: u32 = len - 1_u32 - i as u32;
        if count > &(total / 2) {
            gamma += 2_i32.pow(bit_idx);
        } else {
            println!("1 is most least, adding to gamma, {}", 2_i32.pow(bit_idx));

            epsilon += 2_i32.pow(bit_idx);
        }
    }
    println!("{} {}", gamma, epsilon);
    println!("{}", gamma * epsilon);

    // Part2
}

fn parse_line(mut counts: Vec<u32>, line: &str) -> Vec<u32> {
    for (idx, c) in line.chars().enumerate() {
        let val: u32 = c.to_digit(10).unwrap();
        counts[idx] += val;
    }

    counts
}

fn part2() {
    let str = include_str!("day3_input");
    let len: u32 = str.lines().next().unwrap().len() as u32;

    let mut lines: Vec<&str> = str.lines().collect();

    let mut total: u32 = 0;
    let mut pos: u32 = 0;
    while lines.len() > 1 {
        total = lines.len() as u32;
        let most_common = get_most_common_position(&lines, pos, total);
        println!("most common in pos {}: {}", pos, most_common);
        lines = filter_by_pos(lines, pos.try_into().unwrap(), most_common);
        println!("{:#?}", lines);
        pos += 1;
    }

    let oxygen = isize::from_str_radix(lines[0], 2).unwrap();
    println!("{}", oxygen);

    let str = include_str!("day3_input");
    lines = str.lines().collect();

    total = 0;
    pos = 0;
    while lines.len() > 1 {
        total = lines.len() as u32;
        let most_common = get_least_common_position(&lines, pos, total);
        println!("most common in pos {}: {}", pos, most_common);
        lines = filter_by_pos(lines, pos.try_into().unwrap(), most_common);
        println!("{:#?}", lines);
        pos += 1;
    }

    let co2 = isize::from_str_radix(lines[0], 2).unwrap();
    println!("{}", co2);

    println!("{}", oxygen * co2);
}

fn get_most_common_position(lines: &Vec<&str>, pos: u32, total: u32) -> char {
    let mut count_of_ones: u32 = 0;
    for l in lines {
        if l.chars().nth(pos.try_into().unwrap()).unwrap() == '1' {
            count_of_ones += 1;
        }
    }

    println!("count of ones: {}", count_of_ones);
    if count_of_ones * 2 == total {
        '1'
    } else if count_of_ones > total / 2 {
        '1'
    } else {
        '0'
    }
}

fn get_least_common_position(lines: &Vec<&str>, pos: u32, total: u32) -> char {
    let mut count_of_ones: u32 = 0;
    for l in lines {
        if l.chars().nth(pos.try_into().unwrap()).unwrap() == '1' {
            count_of_ones += 1;
        }
    }

    println!("count of ones: {}", count_of_ones);
    if count_of_ones * 2 == total {
        '0'
    } else if count_of_ones > total / 2 {
        '0'
    } else {
        '1'
    }
}

fn filter_by_pos(lines: Vec<&str>, pos: usize, val: char) -> Vec<&str> {
    println!("{:#?}", lines);
    lines
        .into_iter()
        .filter(|&l| l.chars().nth(pos).unwrap() == val)
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        part2();
    }
}
