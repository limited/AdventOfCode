#!/usr/bin/env python3

# Start: 11:16AM
# Based on day 2 code
# Stop: 1:41, but took some detours for work and school pickup

# Code is now BADLY in need of cleanup/refactoring, lots of dupe in the param/immediate mode and input parsing
import sys

def read_input():
    with open('game_input', 'r') as f:
        pinput = f.readline().rstrip()
        return [int(x) for x in pinput.split(',')]

def output(x):
    print("Output:", x)
    if x != 0:
        print("-------WARNING!---------")
        

def execute(pinput):
    new_start = 0
    count = 0
    
    while True:
        count += 1
                
        #print("Input", pinput)
        #print("Instruction Pointer", new_start)
        opcode = pinput[new_start] % 100
        param_mode = str(pinput[new_start]).zfill(5)
        inst_len = {99: 0,   1: 3,   2: 3,
                    3: 1,    4: 1,   5: 2,
                    6: 2,    7: 3,   8: 3}
        print(f"c:{count} n:{new_start} o:{opcode} p:{param_mode} {pinput[new_start+1]} {pinput[new_start+2]} {pinput[new_start+3]}")
        
        r = pinput[new_start + 1:new_start + 4]
        for idx, reg in enumerate(r):
            if idx > inst_len[opcode] - 1:
                break
            
            if param_mode[2-idx] == "0":
                print(f"--{idx} pos @{reg} = {pinput[reg]}")
                r[idx] = pinput[reg]
            

        if opcode == 99:
            print("HALT")
            break

        elif opcode == 1: # ADD Opcode
            print(f"storing {r[0]} + {r[1]} to @{r[2]}")
            pinput[r[2]] = r[0]+r[1]

        elif opcode == 2: # MULT Opcode
            #print(f"Setting {mult_idx} to {m1} * {m2}")
            pinput[r[2]] = r[0]*r[1]

        elif opcode == 3:
            print(f"Setting pos @{r[0]} to 5")
            pinput[r[0]] = int(input(">>"))

        elif opcode == 4:
            output(r[0])                

        elif opcode == 5:
            if (r[0] != 0):
                print(f"jumping to @{r[1]}")
                new_start = r[1]
                continue
            
        elif opcode == 6:
            if (r[0] == 0):
                print(f"jumping to {r[1]}")
                new_start = r[1]
                continue

        elif opcode == 7:
            pinput[new_start+3] = 1 if (r[0] < r[1]) else 0

        elif opcode == 8:
            pinput[new_start+3] = 1 if (r[0] == r[1]) else 0

        else:
            print("INVALID OPCODE:", opcode)
            break

        new_start += inst_len[opcode] + 1

    return pinput[0]

def main():
    pinput = read_input()
    execute(pinput)

if __name__ == '__main__':
    main()
