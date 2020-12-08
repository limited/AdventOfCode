#!/usr/bin/env python3

import copy

with open('game_input', 'r') as f:
    prog = [l.rstrip().split(" ") for l in f.readlines()]

def execute(prog):
    ip_list = list()
    ip = 0
    acc = 0

    while ip not in ip_list and ip < len(prog):
        ip_list.append(ip)
        arg = int(prog[ip][1])
    
        if prog[ip][0] == "nop":
            ip += 1
        elif prog[ip][0] == "acc":
            ip += 1
            acc += arg
        elif prog[ip][0] == "jmp":
            ip += arg

    return(acc, ip_list)

# Part 1
print("Final acc", execute(prog)[0])

# Part 2
for i in range(0, len(prog)):
    fresh_list = copy.deepcopy(prog)

    if fresh_list[i][0] == "acc":
        continue
    elif fresh_list[i][0] == "jmp":
        fresh_list[i][0] = "nop"
    else:
        fresh_list[i][0] = "jmp"

#    print(fresh_list)
    (acc, ipl) = execute(fresh_list)
    #print(acc, ipl)
    if len(ipl)>2 and len(fresh_list)-2 == ipl[-2]:
        print("Second to final executed!")
        print("Final acc", acc)
        break    



