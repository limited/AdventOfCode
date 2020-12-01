#!/usr/bin/env python3

import itertools
import functools

with open('game_input', 'r') as f:
    inp = map(int, f.readlines())
    
def mult_sums(inp, qty):
    for nums in itertools.permutations(inp, qty):
        if sum(nums) == 2020:
            print(functools.reduce(lambda x,y: x*y, nums))
            break

inp = list(inp)    
mult_sums(inp, 2)
mult_sums(inp, 3)
