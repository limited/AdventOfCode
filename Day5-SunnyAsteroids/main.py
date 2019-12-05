#!/usr/bin/env python3

# Start: 11:16AM
# Based on day 2 code

import sys

def read_input():
    with open('game_input', 'r') as f:
        pinput = f.readline().rstrip()
        return [int(x) for x in pinput.split(',')]

def output(x):
    print("Output:", x)
    if x != 0:
        print("WARNING!")
        

def execute(pinput):
    new_start = 0
    count = 0
    
    while True:
        count += 1
                
        #print("Input", pinput)
        #print("Instruction Pointer", new_start)
        opcode = pinput[new_start] % 100
        param_mode = str(pinput[new_start]).zfill(5)
        print(f"c:{count} n:{new_start} o:{opcode} p:{param_mode} {pinput[new_start+1]} {pinput[new_start+2]} {pinput[new_start+3]}")
        if opcode == 99:
            print("HALT")
            break

        elif opcode == 1: # ADD Opcode
            (add_idx1, add_idx2, sum_idx) = pinput[new_start + 1:new_start + 4]
            print(add_idx1, add_idx2, sum_idx)
            if param_mode[2] == "1":
                add1 = add_idx1
                print("--1 imm mode", add_idx1)
            else:
                add1 = pinput[add_idx1]
                print("--1 pos", add_idx1)

            if param_mode[1] == "1":
                add2 = add_idx2
                print("--2 imm", add_idx2)
            else:
                add2 = pinput[add_idx2]
                print("--2 pos", add_idx2)

            if param_mode[0] == "1":
                print("ERROR, immediate mode for output")

            print(f"storing {add1} + {add2} to {sum_idx}")
            pinput[sum_idx] = add1 + add2
            new_start += 4

        elif opcode == 2: # MULT Opcode
            #print("in", pinput[new_start + 1:new_start + 4])
            (mult_in1, mult_in2, mult_idx) = pinput[new_start+1:new_start+4]
            if param_mode[2] == "1":
                print("--1 imm", mult_in1)
                m1 = mult_in1
            else:
                print("--1 pos", mult_in1)
                m1 = pinput[mult_in1]

            if param_mode[1] == "1":
                print("--2 imm", mult_in2)
                m2 = mult_in2
            else:
                print("--2 pos", mult_in2)
                m2 = pinput[mult_in2]

            if param_mode[0] == "1":
                print("ERROR2, immediate mode for output")                
                
            #print(mult_in1, mult_in2, mult_idx)
            print(f"Setting {mult_idx} to {m1} * {m2}")
            pinput[mult_idx] = m1 * m2
            new_start += 4

        elif opcode == 3:
            out_idx = pinput[new_start+1]
            print(f"Setting pos {out_idx} to 1")
            pinput[out_idx] = int(input(">>"))
            new_start += 2

        elif opcode == 4:
            out_idx = pinput[new_start+1]
            
            if param_mode[2] == "1":
                output(out_idx)
            else:
                print(f"Outputting at {out_idx}")
                output(pinput[out_idx])
                
            new_start += 2

        else:
            print("INVALID OPCODE:", opcode)
            break

    return pinput[0]

def main():
    pinput = read_input()
    execute(pinput)

if __name__ == '__main__':
    main()
