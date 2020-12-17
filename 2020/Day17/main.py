#!/usr/bin/env python3

from collections import defaultdict
from itertools import product
import sys

    
def get_active_neighbors(grid, point):
    active = 0
    for offset in product([-1, 0, 1], repeat=3):
        neigh = (point[0] + offset[0], point[1]+offset[1], point[2]+offset[2])
        if neigh != point and grid[neigh]:
            active += 1

    return(active)


def print_grid(grid, bounds):
    for z in range(bounds[4], bounds[5]+1):
        print("z=",z)
        for x in range(bounds[0], bounds[1]+1):
            for y in range(bounds[2], bounds[3]+1):
                print('#' if grid[(x,y,z)] else '.', end='')
            print()
        print()



grid = defaultdict(bool)

z = 0
with open('game_input', 'r') as f:
    for x,l in enumerate(f.readlines()):
        for y,c in enumerate(l.rstrip()):
            
            if c == '#':
                grid[(x,y,0)] = True
bounds = (0, x, 0, y, 0, z)

boot_rounds = 6
for rnd in range(0, boot_rounds):
    bounds = (bounds[0] - 1, bounds[1] + 1,
              bounds[2] - 1, bounds[3] + 1,
              bounds[4] - 1, bounds[5] + 1)
    next_grid = defaultdict(bool)
    print(bounds)

    for z in range (bounds[4], bounds[5]+1):
        for x in range(bounds[0], bounds[1]+1):
            for y in range(bounds[2], bounds[3]+1):

                act_neigh = get_active_neighbors(grid, (x,y,z))
                print(x,y,z, grid[(x,y,z)], act_neigh)
                if grid[(x,y,z)]:
                    if (act_neigh == 2 or act_neigh == 3):
                        #print(x,y,z, "T")
                        next_grid[(x,y,z)] = True
                        
                else:
                    if act_neigh == 3:
                        #print(x,y,z, "T")
                        next_grid[(x,y,z)] = True
#        print()
                
    grid = next_grid
    #print_grid(grid, bounds)

print(sum(next_grid.values()))
                        
                        
                    
                    
        

    


    
