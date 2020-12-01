#!/usr/bin/env python3

def read_input(name):
    init_mem = [0 for x in range(0,5000000)]
    
    with open(name, 'r') as f:
        pinput = f.readline().rstrip()
        for i, x in enumerate(pinput.split(',')):
            init_mem[i] = int(x)
            
    return init_mem

def execute(mem, input_val, pc=0, relative_base = 0):
    count = 0
    
    while True:
        count += 1
        
        opcode = mem[pc] % 100
        if opcode == 99:
            return (True, None, pc, relative_base)
        
        param_mode = str(mem[pc]).zfill(5)
        inst_len = {1: 3, 2: 3, 3: 1,
                    4: 1, 5: 2, 6: 2,
                    7: 3, 8: 3, 9: 1}
        
        #print(f"c:{count} pc:{pc} o:{opcode} p:{param_mode} {mem[pc+1]} {mem[pc+2]} {mem[pc+3]}")
        
        r = mem[pc+1 : pc+4]
        #print(f"regs: {r}")
        
        for x in range(2, 2-inst_len[opcode], -1):
            if param_mode[x] == "0":
                #print(f"--{x} positional mode, reading @{r[2-x]}")
                r[2-x] = mem[r[2-x]]
                
            elif param_mode[x] == "1":
                #print(f"--{x} immediate mode, using {r[2-x]}")
                pass
            
            elif param_mode[x] == "2":
                #print(f"--{x} relative mode, reading @{r[2-x]}+{relative_base}")
                r[2-x] = mem[r[2-x]+relative_base]

        #print(f"regs: {r}")
                    
        if param_mode[0] == "1":
            print("ERROR, immediate mode for output")
        
        if opcode == 1: # ADD Opcode
            if param_mode[0] == "2":
                #print(f"storing {r[0]} + {r[1]} to {mem[pc+3]}+{relative_base}")
                mem[mem[pc+3]+relative_base] = r[0] + r[1]                
            else:
                #print(f"storing {r[0]} + {r[1]} to {mem[pc+3]}")
                mem[mem[pc+3]] = r[0] + r[1]

        elif opcode == 2: # MULT Opcode
            if param_mode[0] == "2":
                mem[mem[pc+3]+relative_base] = r[0] * r[1]
            else:
                #print(f"Storing {r[0]} * {r[1]} to {mem[pc+3]}")  
                mem[mem[pc+3]] = r[0] * r[1]

        elif opcode == 3:
            val = int(input_val)
            if param_mode[2] == "2":
                #print(f"Setting pos {mem[pc+1]}+{relative_base} to {val}")
                mem[mem[pc+1]+relative_base] = val
            else:
                #print(f"Setting pos {mem[pc+1]} to {val}")
                mem[mem[pc+1]] = val

        elif opcode == 4:
            #print(f"Outputting {r[0]}")
            #print(r[0])
            return (False, r[0], pc+2, relative_base)

        elif opcode == 5:
            if (r[0] != 0):
                #print(f"jumping to {r2}")
                pc = r[1]
                continue
            
        elif opcode == 6:
            if (r[0] == 0):
                #print(f"jumping to {r[1]}")
                pc = r[1]
                continue

        elif opcode == 7:
            if param_mode[0] == "2":
                mem[mem[pc+3]+relative_base] = 1 if (r[0] < r[1]) else 0        
            else:
                mem[mem[pc+3]] = 1 if (r[0] < r[1]) else 0

        elif opcode == 8:
            if param_mode[0] == "2":
                mem[mem[pc+3]+relative_base] = 1 if (r[0] == r[1]) else 0 
            else:            
                mem[mem[pc+3]] = 1 if (r[0] == r[1]) else 0
                   
        elif opcode == 9:
            relative_base += r[0]
            #print(f"Adjusting relative base to {relative_base}")

        else:
            print("INVALID OPCODE:", opcode)            
            break

        pc += inst_len[opcode]+1

    return mem[0]

def find_cross(scaf):
    cross_pos = [(0,1), (0,-1), (1,0), (-1,0)]

    alignment = 0
    
    for s in scaf.keys():
        # This line makes me love python
        nextdoor = [(s[0]+n[0], s[1]+n[1]) in scaf for n in cross_pos]
        if all(nextdoor):
            alignment += s[0]*s[1]

    return alignment

def main():
    mem = read_input('game_input')
    mem[0] = 2
    pc = 0
    rb = 0
    pos = (0,0)
    scaf = dict()
    
    halt = False
    while not halt:
        (halt, out, pc, rb) =  execute(mem, 0, pc, rb)
        if halt:
            break

        # Newline
        if out == 10:
            pos = (0, pos[1] + 1)
            continue
            
        if out != 46:
            scaf[pos] = chr(out)
            
        pos  = (pos[0]+1, pos[1])

    print(find_cross(scaf))
    # Too high 220010

    

        
                




if __name__=='__main__':
    main()
        
        
