#!/usr/bin/env python3

import itertools
from collections import Counter

import re
import sys

def main():
    with open('game_input', 'r') as f:
        inp = f.readlines()

    valid = 0
    valid_part2 = 0
    for l in inp:
        r = re.match("(\d+)-(\d+) (\w): (\w+)", l)
        if r is None:
            sys.exit("bad regex")

        lower = int(r.group(1))
        upper = int(r.group(2))
        word = r.group(4)
        target = r.group(3)            

        cnt = Counter(word)

        if (cnt[target] >= lower and \
            cnt[target] <= upper):
            valid += 1

        # convert to 1 based idx per challenge
        single_cnt = Counter(word[lower-1]+word[upper-1])
        if single_cnt[target] == 1:
            valid_part2 += 1

    print("Part 1", valid)
    print("Part 2", valid_part2)
    
if __name__ == '__main__':
    main()
    
