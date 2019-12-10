#!/usr/bin/env python3
# Start: 9:30AM
import pprint
import math

def read_input(name):
    amap = list()
    adir = dict()
    
    with open(name, 'r') as f:
        for row, line in enumerate(f):
            for col, cell in enumerate(line.rstrip()):
                if cell == "#":
                    adir[(col, row)] = True
                
            row = [1 if l == "#" else 0 for l in line.rstrip()]
            amap.append(row)

    return (amap, adir, len(amap[0]), len(amap))

def count_vis(adir, a, x_size, y_size):
    vec_set = set()
    #print(f"Checking {a}")

    for b in adir.keys():
        if a == b:
            continue
        
        d_x = a[0] - b[0]
        d_y = a[1] - b[1]
        vec = math.atan2(d_y, d_x)
        #if (d_y == 0):
        #    if (d_x > 0):
        #        vec = 'left'
        #    else:
        #        vec = 'right'
        #        
        #elif d_x == 0:
        #    if d_y > 0:
        #        vec = 'up'
        #    else:
        #        vec = 'down'
        #else:
        #    vec = d_y/d_x


        #print(f"Adding vec {vec} from {b}")
        #if vec in vec_set:
        #    print(f"--EXISTS")
            
        vec_set.add(vec)
    return len(vec_set)
    #return sum([is_vis(adir, a,b) for b in adir.keys()])

def main():
    amap, adir, x_size, y_size = read_input('game_input')
    #for a in adir.keys():
    #    vis = count_vis(adir, a, x_size, y_size)
    #    print("-------------Visible from",a,vis)
    print("ANSWER", max([count_vis(adir, a, x_size, y_size) for a in adir.keys()]))

if __name__ == '__main__':
    main()
