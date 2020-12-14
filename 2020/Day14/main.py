#!/usr/bin/env python3

import re

# Part 1
mem = dict()
with open('game_input', 'r') as f:
    for line in f:
        if line.startswith("mask"):
            mask = line.rstrip().split(' ')[2]
            ands = int(mask.replace('X', '1'), 2)
            ors  = int(mask.replace('X', '0'), 2)
                       
            #print("mask", mask)
            #print("ands", ands)
            #print("ors " ,ors)
            
        elif line.startswith("mem"):
            m = re.match("mem\[(\d+)\] = (\d+)", line.rstrip())
            if m is not None:
                addr = int(m.group(1))
                val = int(m.group(2))
                mem[addr] = (val & ands) | ors
                #print("write mem ", addr, val, mem[addr])

    print(sum(mem.values()))


# Part 2
def x_replace(mask, repfields):
#    print("subbing from ", mask)
    sub_and = mask.replace('0', '1')
    sub_or = mask.replace('1', '0')    
    for x in repfields:
        sub_and = sub_and.replace('X', x, 1)
        sub_or = sub_or.replace('X', x, 1)
        
    return (int(sub_and, 2), int(sub_or, 2))
    
import itertools
mem = dict()
with open('game_input', 'r') as f:
    for line in f:
        if line.startswith("mask"):
            mask = line.rstrip().split(' ')[2]
            ors  = int(mask.replace('X', '0'), 2)

            num_x = len(mask.replace('0', '').replace('1', ''))
            #print("mask", mask)
            #print("ors  {0:036b}".format(ors))
            #print("num_x",num_x)
            x_rep = [x for x in itertools.product('01', repeat=num_x)]
            #print(x_rep)
                       
        elif line.startswith("mem"):
            m = re.match("mem\[(\d+)\] = (\d+)", line.rstrip())
            if m is not None:
                addr = int(m.group(1))
                #print("addr {0:036b}".format(addr))
                val = int(m.group(2))
                addr = addr | ors
                #print("addr {0:036b}".format(addr))
                for a in x_rep:
                    (sub_and, sub_or) = x_replace(mask, a)
                    sub_addr = (addr & sub_and) | sub_or
                    #print("writ {0:036b}".format(sub_addr), end ='')
                    #print(" ",sub_addr)
                    mem[sub_addr] = val
                #print()
        


    print(sum(mem.values()))
                
