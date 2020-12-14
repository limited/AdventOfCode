#!/usr/bin/env python3

import math
import time
import sys

with open('game_input', 'r') as f:
    earliest = int(f.readline().rstrip())
    raw_ids  = f.readline().rstrip().split(',')
    ids = filter(lambda x: x != 'x', raw_ids)
    ids = [int(x) for x in ids]

# Part 1 (2 solutions)
# First timestamp to hit mod 0
start = time.time()
ts = earliest
run = True
while run:
    for bid in ids:
        if ts % bid == 0:
            print((ts-earliest)*bid)
            run = False
            break
        
    ts += 1
end = time.time()
#print(end-start)

# or ceil(earliest/id)*id
start = time.time()
next_bus = [math.ceil(earliest/bid)*bid for bid in ids]
lowest_wait = sorted(next_bus)[0]
bid = ids[next_bus.index(lowest_wait)]
print((lowest_wait - earliest)*bid)
end = time.time()
#print(end - start)

# Part 2
# Kicked my butt, needed hints:
# 1) https://todd.ginsberg.com/post/advent-of-code/2020/day13/
# OR
# 2) Chinese Remainder Theorem (https://www.youtube.com/watch?v=zIFehsBHB8o) and
#    Multiplicative modular inverse (https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/)
offsets = {bid: -1*raw_ids.index(str(bid)) for bid in ids}

import crt
inp = [(off, bid) for bid,off in offsets.items()]
print(inp)
print(crt.crt(inp))

    
    
            


 
