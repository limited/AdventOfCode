#!/usr/bin/env python3
# Start: 6:32AM
# Part1: 6:55AM, feelin good
# Part2: Pause at 7:22,ick. Went for a run, unpause around 8 done at 8:10AM
# Total time, maybe ~1hr
#Day       Time   Rank  Score       Time   Rank  Score
#  7   06:55:00   6712      0   08:10:12   4147      0


import sys
from itertools import permutations

def read_input(name):
    with open(name, 'r') as f:
        pinput = f.readline().rstrip()
        return [int(x) for x in pinput.split(',')]

def output(x):
    print("Output:", x)
    if x != 0:
        print("-------WARNING!---------")
        

def execute(pinput, user_in, pc, last_output):
    new_start = pc
    count = 0
    
    while True:
        count += 1
                
        #print("Input", pinput)
        #print("Instruction Pointer", new_start)
        opcode = pinput[new_start] % 100
        param_mode = str(pinput[new_start]).zfill(5)
        #print(f"c:{count} n:{new_start} o:{opcode} p:{param_mode} {pinput[new_start+1]} {pinput[new_start+2]} {pinput[new_start+3]}")
        if opcode == 99:
            return (True, last_output, 0)

        elif opcode == 1: # ADD Opcode
            (add_idx1, add_idx2, sum_idx) = pinput[new_start + 1:new_start + 4]
            #print(add_idx1, add_idx2, sum_idx)
            if param_mode[2] == "1":
                add1 = add_idx1
                #print("--1 imm mode", add_idx1)
            else:
                add1 = pinput[add_idx1]
                #print("--1 pos", add_idx1)

            if param_mode[1] == "1":
                add2 = add_idx2
                #print("--2 imm", add_idx2)
            else:
                add2 = pinput[add_idx2]
                #print("--2 pos", add_idx2)

            if param_mode[0] == "1":
                print("ERROR, immediate mode for output")

            #print(f"storing {add1} + {add2} to {sum_idx}")
            pinput[sum_idx] = add1 + add2
            new_start += 4

        elif opcode == 2: # MULT Opcode
            #print("in", pinput[new_start + 1:new_start + 4])
            (mult_in1, mult_in2, mult_idx) = pinput[new_start+1:new_start+4]
            if param_mode[2] == "1":
                #print("--1 imm", mult_in1)
                m1 = mult_in1
            else:
                #print("--1 pos", mult_in1)
                m1 = pinput[mult_in1]

            if param_mode[1] == "1":
                #print("--2 imm", mult_in2)
                m2 = mult_in2
            else:
                #print("--2 pos", mult_in2)
                m2 = pinput[mult_in2]

            if param_mode[0] == "1":
                print("ERROR2, immediate mode for output")                
                
            #print(mult_in1, mult_in2, mult_idx)
            #print(f"Setting {mult_idx} to {m1} * {m2}")
            pinput[mult_idx] = m1 * m2
            new_start += 4

        elif opcode == 3:
            out_idx = pinput[new_start+1]
            #print(f"Setting pos {out_idx} to 1")
            pinput[out_idx] = user_in.pop(0)
            new_start += 2

        elif opcode == 4:
            out_idx = pinput[new_start+1]
            
            if param_mode[2] == "1":
                last_output = out_idx
            else:
                #print(f"Outputting at {out_idx}")
                last_output = pinput[out_idx]
            
            return (False, last_output, new_start + 2)
            #new_start += 2

        elif opcode == 5:
            (r1, r2) = pinput[new_start+1:new_start+3]
            if param_mode[2] == "0":
                #print(f"--pos mode {r1} {pinput[r1]}")
                r1 = pinput[r1]

            if param_mode[1] == "0":
                r2 = pinput[r2]
                
            if (r1 != 0):
                #print(f"jumping to {r2}")
                new_start = r2
                continue
    
            new_start += 3
            
        elif opcode == 6:
            (r1, r2) = pinput[new_start+1:new_start+3]
            if param_mode[2] == "0":
                r1 = pinput[r1]

            if param_mode[1] == "0":
                r2 = pinput[r2]
                
            if (r1 == 0):
                #print(f"jumping to {r2}")
                new_start = r2
                continue

            new_start += 3

        elif opcode == 7:
            (r1, r2, r3) = pinput[new_start+1:new_start+4]
            if param_mode[2] == "0":
                r1 = pinput[r1]

            if param_mode[1] == "0":
                r2 = pinput[r2]
                
            pinput[r3] = 1 if (r1 < r2) else 0
            new_start += 4

        elif opcode == 8:
            (r1, r2, r3) = pinput[new_start+1:new_start+4]
            if param_mode[2] == "0":
                r1 = pinput[r1]

            if param_mode[1] == "0":
                r2 = pinput[r2]
                
            pinput[r3] = 1 if (r1 == r2) else 0
            new_start += 4            

        else:
            print("INVALID OPCODE:", opcode)
            break

    return pinput[0]

def main():
    pinput = read_input('game_input')
    #pinput = read_input('test5')

    max_sig = 0
    max_phase = None
    #phase_list = [0,1,2,3,4]
    #for phase in permutations(phase_list):
    #    phase = list(phase)
    #    cascade_in = 0
    #    for x in range(0,5):
    #        user_in = [phase.pop(0), cascade_in]
    #        cascade_in = execute(pinput, user_in)
    #
    #    if cascade_in > max_sig:
    #        max_sig = cascade_in
    #        max_phase = phase

    #print("PART 1", max_sig)

    # Part2
    phase_list = [5,6,7,8,9]        
    for phase in permutations(phase_list):
        
        prog_mem = [list(pinput) for x in range(0,5)]
        cascade_in = 0        
        pc = [0,0,0,0,0]
        last_output = [0,0,0,0,0]        
        phase = list(phase)
        
        while True:
            for stage in range(0,5):            
                user_in = list()

                # Only send in phase signals first time through
                if (len(phase) > 0):
                    user_in.append(phase.pop(0))
                user_in.append(cascade_in)
                print(f"Running stage {stage} with input {user_in}")
                (halt, cascade_in, pc[stage]) = execute(prog_mem[stage], user_in, pc[stage], last_output[stage])
                last_output[stage] = cascade_in
                print(f"--Stage {stage} outputs {cascade_in} with prog counters {pc[stage]}, {halt}")
                    
            if halt:
                break

        if cascade_in > max_sig:
            max_sig = cascade_in
            max_phase = phase

    print("MAX SIGNAL",max_sig)
            
if __name__ == '__main__':
    main()
