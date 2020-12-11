#!/usr/bin/env python3
import copy
from collections import Counter
import sys

def print_grid(g):
    for r in g:
        print("".join(r))
    print()
    print()


dirs = [(-1,-1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)]

def get_visible_occupied(grid, row, col):
    count = 0
    #print(row,col)
    for d in dirs:
        #print("  Dir", d)
        r = row + d[0]
        c = col + d[1]
        while ((r >= 0 and r < h) and (c >=0 and c < w)):
            #print(f"   Checking ({r},{c}) == {grid[r][c]}")
            if grid[r][c] == '#':
                count += 1
                break
            elif grid[r][c] == 'L':
                break
            
            
            r += d[0]
            c += d[1]
    return(count)
            

    
def get_adjacent_occupied(grid, row, col):
    count = 0
    for r in range(max(0, row-1), min(h-1, row+1)+1):
        for c in range(max(0, col-1),  min(w-1, col+1)+1):
            if (r != row or c != col) and grid[r][c] == '#':
                count += 1

    return (count)



# tolerance, how many occupied seats before a seat empties
# Part 1 = 4
# Part 2 = 5
def do_cell(grid, r, c):
    #occ = get_adjacent_occupied(grid, r, c) # Part 1
    occ = get_visible_occupied(grid, r, c)
    
    if grid[r][c] == 'L' and occ == 0:
        return ('#', True)
    
    elif grid[r][c] == '#' and occ >= 5: # Part1 4:
        return ('L', True)

    return (grid[r][c], False)


with open('game_input', 'r') as f:
    grid = [list(g.rstrip()) for g in f.readlines()]

h = len(grid) 
w = len(grid[0])

#print_grid(grid)
#print(get_visible_occupied(grid, 4, 3))
#sys.exit(0)


changed = True
round = 0
while changed:
    changed = False
    next_rnd = copy.deepcopy(grid)

    #if round == 3:
        #print("Round ",round)
        #print_grid(grid)
        #print(get_visible_occupied(grid, 0,3))
        #sys.exit(0)

        
    for r in range(0, h):
        for c in range(0, w):
            (next_rnd[r][c], chg) = do_cell(grid, r, c)
            changed = changed or chg

    grid = next_rnd
    #print_grid(grid)

    round += 1
    #print(round)

occ = 0
for r in grid:
    for c in r:
        if c == '#':
            occ += 1
print(occ)

            
