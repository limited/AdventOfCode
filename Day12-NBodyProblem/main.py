#!/usr/bin/env python3

import re
import itertools

#infile='test1'
infile='game_input'

f = open(infile, 'r')

pos = list()
vel = list()
for l in f:
    match = re.match('<x=(-?\d*), y=(-?\d*), z=(-?\d*)>', l.rstrip())
    if match is not None:
        pos.append([int(match.group(1)), int(match.group(2)), int(match.group(3))])
        vel.append([0,0,0])
print(pos)

steps = 1000
for s in range(0, steps):
    #XXX_EF Gravity
    for pair in itertools.combinations(range(0, len(pos)), 2):
        #print(pair)
        for d in range(0, 3):
            #print("D",d, pos[pair[0]][d], pos[pair[1]][d])
            if pos[pair[0]][d] < pos[pair[1]][d]:
                #print("A")
                vel[pair[0]][d] += 1
                vel[pair[1]][d] -= 1
            elif pos[pair[0]][d] == pos[pair[1]][d]:
                pass
            
            else:
                #print("B")
                vel[pair[0]][d] -= 1
                vel[pair[1]][d] += 1


    # Velocity
    for i in range(0, len(pos)):
        for d in range(0,3):
            pos[i][d] = pos[i][d] + vel[i][d]

    #for i in range(0, len(pos)):
    #    print(f"pos=<{pos[i][0]}, {pos[i][1]}, {pos[i][2]}>, vel=<{vel[i][0]}, {vel[i][1]}, {vel[i][2]}>")
    
    
energies = [sum(map(abs, pos[i])) * sum(map(abs, vel[i])) for i in range(0,len(pos))]
print(f"Total Energy: {sum(energies)}")

