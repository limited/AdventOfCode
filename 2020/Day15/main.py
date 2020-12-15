#!/usr/bin/env python3
inp = ['x',0, 3, 6] # Test
inp = ['x', 18,11,9,0,5,1] # Game Input

def rindex(lst, val):
    return len(lst) - 1 - [x for x in reversed(lst)].index(val)
    
    
# Part 1
#print(inp)
while len(inp) <= 2020:
    try:
        nxt = len(inp)-1 - rindex(inp[0:len(inp)-1], inp[-1])
        #print("Last:", inp[-1], " Last Turn #:", len(inp)-1, " Last found at: ", rindex(inp[0:len(inp)-1], inp[-1]), "Next: ", nxt)        
        inp.append(nxt)
    except ValueError:
        #print("Last:", inp[-1], " Last Turn #:", len(inp)-1, " Last found at: <None> Next: 0")      
        inp.append(0)
    #print(inp)

print(inp[2020])

# Part 2 - do the same thing but for len = 30 mil
from collections import defaultdict

#inp = [0, 3, 6]

inp = [18,11,9,0,5,1]
#rounds = 2020
rounds = 30000000

last_index = defaultdict(list)
for idx, val in enumerate(inp):
    last_index[val].append(idx+1)

last = inp[-1]
for i in range(len(inp)+1, rounds+1):
    #if i % 1000000 == 0:
    #    print(i)
    try:
        ri = last_index[last][-2]            
        nxt = i - 1 - ri
    
    except IndexError:
        ri = "<None>"
        nxt = 0

    #print(f"Turn {i}, Last: {last} , Last Found at {ri}, nxt: {nxt}")        
    last = nxt
    last_index[nxt].append(i)
    if len(last_index[nxt]) > 2:
        last_index[nxt].pop(0)

print(last)
