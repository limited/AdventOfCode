#!/usr/bin/env python3
# Start: 9:30AM
import pprint
import math
from collections import defaultdict

def read_input(name):
    adir = dict()
    
    with open(name, 'r') as f:
        for row, line in enumerate(f):
            for col, cell in enumerate(line.rstrip()):
                if cell == "#":
                    adir[(col, row)] = True

    return adir

def count_vis(adir, a):
    vec_set = set()
    
    for b in adir.keys():
        if a == b:
            continue
        
        d_x = a[0] - b[0]
        d_y = a[1] - b[1]
        vec = math.atan2(d_y, d_x)
        vec_set.add(vec)
    return len(vec_set)

def range_asteroids(adir, a):
    ranges = defaultdict(list)
    
    for b in adir.keys():
        if a == b:
            continue
        
        d_x = a[0] - b[0]
        d_y = a[1] - b[1]
        vec = math.atan2(d_y, d_x)
        dist = math.sqrt(d_x**2 + d_y**2)

        ranges[vec].append((dist, b))

    return ranges

def sort_ranges(ranges):
    range_list = list()
    angles = sorted(ranges.keys())
    while angles[0] < math.pi/2:
        angles.append(angles.pop(0))

    for a in angles:
        range_list.append(sorted(ranges[a]))

    print(range_list)
    return range_list
    

# Input is a list of lists of tuple. Tuple is (distance, (x,y))
# First item in outer list corresponds to up direction (pi/2?)
def fire_away(range_list, n):
    total_zaps = n
    angle_idx = 0
    last_coord = None
    
    while n > 0:
        if len(range_list[angle_idx]) > 0:
            last_coord = range_list[angle_idx].pop(0)[1]
            print(f"{total_zaps-n} Zapping {last_coord}")
            n -= 1

        angle_idx = (angle_idx + 1) % len(range_list)
        
    return last_coord

def main():
    adir = read_input('game_input')

    # Part1
    print("Part 1 Answer:", max([count_vis(adir, a) for a in adir.keys()]))

    # Part2
    coords = None
    max_val = 0
    for a in adir.keys():
        val = count_vis(adir, a)
        if (val > max_val):
            coords = a
            max_val = val
    #coords=(8,3)
    print(f"Station located at {coords} w/ value {max_val}")

    ranges = range_asteroids(adir, coords)
    range_list = sort_ranges(ranges)
    nth_coord = fire_away(range_list,200)
    
    print(nth_coord)
    print(f"{nth_coord[0]*100+nth_coord[1]}")

if __name__ == '__main__':
    main()
