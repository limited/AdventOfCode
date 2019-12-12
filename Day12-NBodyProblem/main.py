#!/usr/bin/env python3
# Needed hints on
# a) cycle w/ init position
# b) using LCM of indepdent axis cycle lengths

import re
import itertools
import numpy

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


init_state = list()
cycle_length = [0,0,0]
for d in range(0,3):
    init_state.append([body[d] for body in pos])
    init_state[d].extend([body[d] for body in vel])
print(init_state)

count = 0
run = True
while run:
    # Gravity
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

    count += 1
    
    # Check cycle in any axis
    # XXX_EF Might need to include velocity in state check
    for d in range(0,3):
        axis_state = [body[d] for body in pos]
        axis_state.extend([body[d] for body in vel])
        if cycle_length[d] == 0 and axis_state == init_state[d]:
            print(f"Found cycle in axis {d} at step {count}")
            cycle_length[d] = count
            if 0 not in cycle_length:
                run = False



    #for i in range(0, len(pos)):
    #    print(f"pos=<{pos[i][0]}, {pos[i][1]}, {pos[i][2]}>, vel=<{vel[i][0]}, {vel[i][1]}, {vel[i][2]}>")
        
energies = [sum(map(abs, pos[i])) * sum(map(abs, vel[i])) for i in range(0,len(pos))]
print(f"Total Energy: {sum(energies)}")

print(cycle_length)
print(numpy.lcm.reduce(cycle_length))
# 43156306344996 too low (had count in wrong spot)
# 43156306344996 too low
# 420788524631496 !!!

#6732500091353405 too high (doing velocity state check wrong)


