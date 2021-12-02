use std::fs;

mod day2;

fn main() {
    let inp = fs::read_to_string("input").unwrap();

    let inp_lines = inp.split("\n");
    let mut inp_iter = inp_lines.clone();
    let mut last: u32 = inp_iter.next().expect("no vals").parse().unwrap();
    let mut increases = 0;

    for x in inp_iter {
        let val = x.parse().unwrap();
        if val > last {
            increases += 1;
        }

        last = val;
    }

    println!("Increases: {}", increases);
    increases = -1; // First one always seen as an increase because compare is against 0

    let inp_vec: Vec<u32> = inp_lines.map(|v| v.parse().unwrap()).collect();
    last = 0;

    for x in inp_vec.windows(3) {
        println!("{:#?}", x);
        let sum = x.iter().sum();
        if sum > last {
            increases += 1;
            println!("increased");
        }
        last = sum;
    }

    println!("Windowed increases: {}", increases);
}

// 3434 too high, needed to reset increases
// 1738 too high
