#!/usr/bin/env python3

import sys

with open('game_input', 'r') as f:
    trees = [l.rstrip() for l in f]

        
print(trees)        
        
width = len(trees[0])

def check_slope(right, down):
    print(right, down)
    x = 0
    count = 0

    for (ridx, row) in enumerate(trees):
        if (ridx % down != 0):
            continue
        #print(row)
        #print(x, row[x] == '#')
        if row[x] == '#':
            count += 1
            
        x = (x+right) % width
    return (count)

print(check_slope(3,1))

tree_count = 1
for s in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    out = check_slope(*s)
    tree_count = tree_count * out

print(tree_count)
    
    
