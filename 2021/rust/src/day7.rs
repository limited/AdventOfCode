pub fn part1() -> i32 {
    let mut crabs: Vec<i32> = include_str!("day7_input")
        .split(",")
        .map(|f| f.parse().unwrap())
        .collect();

    crabs.sort();
    let len:usize = crabs.len();
    let median:i32 = if len % 2 == 0 {
        crabs[len/2]
    } else {
        crabs[len/2 + 1]
    };
    println!("picking median {}", median);

    crabs.iter().fold(0, |acc, &c| {
        println!("{} {}", acc, c);
        acc + (median - c).abs()
    })
}

pub fn part2() -> i32 {
    let crabs: Vec<i32> = include_str!("day7_test_input")
    .split(",")
    .map(|f| f.parse().unwrap())
    .collect();

    let maxval = crabs.iter().max().unwrap();
    println!("maxval {}", *maxval);

    let mut costs:Vec<i32> = vec![0; *maxval+1];
    for c in 1..(*maxval) {
        if c == 1{
            costs[c as usize] = 1;
        } else {
            costs[c as usize] = costs[c as usize-1] + c;
        }
    }


    let mut min_fuel = 2147483647;
    let mut min_pos = 2147483647;
    for x in 0..(*maxval-1) {
        let mut tot_fuel = 0;
        for c in &crabs {
            let idx = (x-c).abs() as usize;
            println!("idx {} {} {}", idx, x, c);
            tot_fuel += costs[idx];
        }

        if tot_fuel < min_fuel {
            min_fuel = tot_fuel;
            min_pos = x;
        }
    }

    min_fuel
}

#[cfg(test)]
mod tests {
    use super::*;

    //#[test]
    fn test_part1() {
        
        println!("Part 1: {}", part1());
    }

    #[test]
    fn test_part2() {
        println!("Part 2: {}", part2());
    }
}
