#!/usr/bin/env python3
# UGH, needed a hint from reddit about handle to handle negative numbers. The grid doesn't wrap around, its a 4 quadrant coordinate space
# Also picked up using a dict as a sparse representation from reddit. 
from collections import defaultdict

def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.rstrip().split(',') for l in f]
        
        return lines

def update_grid(grid, cur_y, cur_x, steps):
    if (cur_y, cur_x) not in grid:
        grid[(cur_y,cur_x)] =  steps
    
def fill_grid(grid, wires):
    min_distance = 5000000
    grid = [{},{}]
    
    for (idx, wire) in enumerate(wires):
        val = 1 << idx
        cur_x = 0
        cur_y = 0
        steps = 0
        print("new wire", idx, val)        
        
        for inst in wire:
            dir = inst[0]
            count = int(inst[1:])
            print(dir,count)
            if dir == 'U':
                for i in range(0,count):
                    steps += 1
                    cur_y += 1
                    update_grid(grid[idx], cur_y, cur_x, steps)

            elif dir == 'R':
                for i in range(0,count):
                    steps += 1                    
                    cur_x += 1
                    update_grid(grid[idx], cur_y, cur_x, steps)                    
                    
            elif dir == 'L':
                for i in range(0,count):
                    steps += 1                    
                    cur_x -= 1
                    update_grid(grid[idx], cur_y, cur_x, steps)                    
                    
            elif dir == 'D':
                for i in range(0,count):
                    steps += 1                    
                    cur_y -= 1
                    update_grid(grid[idx], cur_y, cur_x, steps)                    

            else:
                raise RuntimeError("Unknown Direction: "+dir)
            #print(grid[idx])

    check_intersection_steps(grid)


    #for v in grid.values():
    #    if v == 3:
    #        print("FOUND A 3")
    #print(f"Min Distance: {min_distance}")

def check_intersection_manhattan(grid, cur_y, cur_x, min_distance):
    if grid[(cur_y,cur_x)] == 3:
        print(f"Intersection at {cur_y},{cur_x}, {abs(cur_y)+abs(cur_x)}")
        min_distance = min(min_distance, abs(cur_x)+abs(cur_y))
    return min_distance

def check_intersection_steps(grid):
    intersections = set(grid[0].keys()) & set(grid[1].keys())
#    print(intersections)
#    for i in intersections:
#        print(f"{i} {grid[0][i]} {grid[1][i]} ")
    
    distances = [grid[0][i]+grid[1][i] for i in intersections]
    print(min(distances))



            
def main():
    grid = defaultdict(int)
    
    wires = read_input('game_input')
    print(wires)

    fill_grid(grid, wires)
    # 3884 too high

    
if __name__ == '__main__':
    main()
