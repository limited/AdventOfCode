#!/usr/bin/env python3

import re
import sys

field_names = list()
fields = list()
all_fields = set()


tickets = list()
flat_tix = list()

mode = 0
with open('test2', 'r') as o:
    for f in o:
        f = f.rstrip()

        if len(f) == 0:
            continue

        if f.startswith("your"):
            mode = 1
            continue
        
        elif f.startswith("nearby"):
            mode = 2
            continue
        
        if mode == 0:
            m = re.match("([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)", f)
            if m is None:
                print("Parse Error ", f)
                sys.exit(0)
                
            field_names.append(m.group(1))
            
            s1 = set()
            s2 = set()
            for x in range(int(m.group(2)), int(m.group(3))+1):
                all_fields.add(x)
                s1.add(x)
                
            for x in range(int(m.group(4)), int(m.group(5))+1):
                all_fields.add(x)
                s2.add(x)

            fields.append((s1, s2))
            
        elif mode == 1:
            yours = [int(x) for x in f.split(',')]
            tickets.append(yours)

        elif mode == 2:
            ticket = [int(x) for x in f.split(',')]
            tickets.append(ticket)
            flat_tix.extend(ticket)

# Part 1
invalid_fields = filter(lambda x: x not in all_fields, flat_tix)
print(sum(invalid_fields))

# Part 2
print(field_names)
print(fields)
print(tickets)

# discard invalid
valid_tix = list()
for t in tickets:
    valid = True
    for f in t:
        if f not in all_fields:
            print("ticket ",t," invalid")
            valid = False
            break
    if valid:
        valid_tix.append(t)

print(len(valid_tix))
    
    
        
        
        
