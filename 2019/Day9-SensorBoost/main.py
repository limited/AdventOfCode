#!/usr/bin/env python3

# Start 8:38AM, ugh more intcode, needed some refactoring
# Done 10:30AM
#      --------Part 1--------   --------Part 2--------
#Day       Time   Rank  Score       Time   Rank  Score
#  9   10:24:34   6436      0   10:28:34   6367      0

def read_input(name):
    init_mem = [0 for x in range(0,5000000)]
    
    with open(name, 'r') as f:
        pinput = f.readline().rstrip()
        for i, x in enumerate(pinput.split(',')):
            init_mem[i] = int(x)
            
    return init_mem

def execute(mem, pc=0):
    count = 0
    relative_base = 0
    
    while True:
        count += 1
        
        opcode = mem[pc] % 100
        if opcode == 99:
            return True
        
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
            val = int(input(">>"))
            if param_mode[2] == "2":
                #print(f"Setting pos {mem[pc+1]}+{relative_base} to {val}")
                mem[mem[pc+1]+relative_base] = val
            else:
                #print(f"Setting pos {mem[pc+1]} to {val}")
                mem[mem[pc+1]] = val

        elif opcode == 4:
            print(f"Outputting {r[0]}")
            print(r[0])
            break

        elif opcode == 5:
            if (r[0] != 0):
                #print(f"jumping to {r2}")
                pc = r[1]
                continue
            
        elif opcode == 6:
            if (r[0] == 0):
                #print(f"jumping to {r2}")
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

def main():
    mem = read_input('game_input')
    execute(mem)
    

if __name__ == '__main__':
    main()
