use counter::Counter;
use std::collections::HashMap;
use std::collections::VecDeque;

pub fn part1() -> usize {
    let mut fish: Vec<u32> = include_str!("day6_test_input")
        .split(",")
        .map(|f| f.parse().unwrap())
        .collect();

    let total_days = 80;

    for _d in 0..total_days {
        let mut new_fish = 0;
        for i in 0..fish.len() {
            if fish[i] == 0 {
                fish[i] = 6;
                new_fish += 1;
            } else {
                fish[i] -= 1;
            }
        }
        let mut new = vec![8; new_fish];
        fish.append(&mut new);
        //println!("After {} days: {:?}", _d + 1, fish);
    }

    fish.iter().len()
}

pub fn part2() -> u64 {
    let fish: Vec<u32> = include_str!("day6_input")
        .split(',')
        .map(|f| f.parse().unwrap())
        .collect();

    let mut bdays: HashMap<u32, usize> = HashMap::new();
    for &f in fish.iter() {
        match bdays.get_mut(&f) {
            Some(v) => *v += 1,
            None => {
                bdays.insert(f, 1);
            }
        }
    }

    let mut new: VecDeque<usize> = VecDeque::from([0, 0]);
    println!("Initial State: {:#?}", bdays);

    let total_days = 256;

    for day in 0..total_days {
        let d = day % 7;

        let v = *bdays.get(&d).unwrap_or(&0);
        new.push_back(v);

        let y = new.pop_front().unwrap();
        println!("Moving over {} to day {}", y, d);
        match bdays.get_mut(&d) {
            Some(x) => *x += y,
            None => {
                bdays.insert(d, y);
            }
        };

        println!("After {} days: {:#?} {:#?}", day + 1, bdays, new);
    }

    let mut total = 0_usize;
    for v in bdays.values() {
        total += v;
    }
    println!("{}", total);

    (total + new.pop_back().unwrap() + new.pop_back().unwrap())
        .try_into()
        .unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let total_fish = part1();
        //println!("{}", total_fish);
    }

    #[test]
    fn test_part2() {
        let total_fish = part2();
        println!("Total Fish: {}", total_fish);
        //1467862910679 too low
    }
}
