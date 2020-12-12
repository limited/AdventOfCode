#!/usr/bin/env python3

#         E  N  Dir
coords = [0, 0, 0]
moves = {'N': [0, 1, 0],
         'S': [0, -1, 0],
         'E': [1, 0, 0],
         'W': [-1, 0, 0],
         'L': [0, 0, -1],
         'R': [0, 0, 1],
         'F': [1, 0, 0]}

dirs = ['E', 'S', 'W', 'N']

# Part 1
with open('game_input', 'r') as f:
    for l in f.readlines():
        (d,v) = (l.rstrip()[0:1], int(l.rstrip()[1:]))
        if d == 'L' or d == 'R':
            coords[2] = ((int(v/90) * (1 if d=='R' else -1)) + coords[2]) % 4
            continue
        
        elif d == 'F':
            d = dirs[coords[2]]
            
        coords = [coords[i]+moves[d][i]*v for i in range(0, len(coords))]
                  
    print(abs(coords[0]) + abs(coords[1]))


# Part 2
#           E   N  Dir
print("----")
waypoint = [10, 1]
coords =   [0,  0, 0]
with open('game_input', 'r') as f:
    for l in f.readlines():
        (d,v) = (l.rstrip()[0:1], int(l.rstrip()[1:]))
        print(d,v)
        if d == 'L':
            v = int(v/90)            
            for i in range(0,v):
                waypoint = [-1 * waypoint[1], waypoint[0]]
        
        elif d == 'R':
            #Prob something simpler w/ a rotation matrix transform
            v = int(v/90)
            for i in range(0,v):
                waypoint = [1 * waypoint[1], -1 * waypoint[0]]
                
        elif d == 'F':
            coords = [coords[i]+waypoint[i]*v for i in range(0, len(waypoint))]

        else:
            waypoint = [waypoint[i]+moves[d][i]*v for i in range(0, len(waypoint))]
        print("Position", coords)
        print("Waypoint", waypoint, end='\n\n')
                  
    print(abs(coords[0]) + abs(coords[1]))


    
