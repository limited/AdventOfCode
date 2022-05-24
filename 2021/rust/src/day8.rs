pub fn part1() -> usize {
    let str = include_str!("./day8_input");

    let easy_lengths = [2, 3, 4, 7];

    let mut total_easy: usize = 0;
    for l in str.lines() {
        let out_digits = l.split(" | ").nth(1).unwrap();
        let easy_count = out_digits
            .split(' ')
            .map(|d| {
                println!("{:?} {}", d, d.len());
                d.len()
            })
            .filter(|l| easy_lengths.contains(l))
            .map(|d| println!("{}", d))
            .count();
        total_easy += easy_count;
    }

    total_easy
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        println!("Part 1: {}", part1());
    }
}
