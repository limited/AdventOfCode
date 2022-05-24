use array2d::Array2D;

pub fn part1() {
    let str = include_str!("./day4_test_input").lines();
    let nums: Vec<i32> = str
        .next()
        .unwrap()
        .split(',')
        .map(|v| v.parse::<i32>())
        .collect();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        part1();
    }
}
