pub fn part1() {
    let str = include_str!("../day2_input");
    let inp: Vec<(i32, i32)> = str
        .lines()
        .map(|l| parse_line(l))
        .map(|(d, v)| process(d, v))
        .collect();

    let mut f = 0;
    let mut d = 0;
    for i in inp {
        f += i.0;
        d += i.1;
    }

    println!("{} {}", f, d);
    println!("{}", f * d);

    // Part2
    f = 0;
    d = 0;
    let mut aim = 0;
    for l in str.lines() {
        let p = parse_line(l);
        match p {
            ("forward", val) => {
                f += val;
                d += aim * val
            }
            ("up", val) => aim -= val,
            ("down", val) => aim += val,
            _ => panic!("unknown direction"),
        };
        //    println!("{} {} {}", f, d, aim);
    }

    println!("{}", f * d);
}

fn parse_line(l: &str) -> (&str, i32) {
    let mut parts = l.splitn(2, ' ');
    (
        parts.next().unwrap(),
        parts.next().unwrap().parse().unwrap(),
    )
}

// (forward, depth)
fn process(dir: &str, val: i32) -> (i32, i32) {
    match dir {
        "forward" => (val, 0),
        "up" => (0, -1 * val),
        "down" => (0, val),
        _ => panic!("unknown direction"),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        part1();
    }
}
