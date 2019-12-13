#!/usr/bin/env python3
import time

def read_input(name):
    init_mem = [0 for x in range(0,5000000)]
    
    with open(name, 'r') as f:
        pinput = f.readline().rstrip()
        for i, x in enumerate(pinput.split(',')):
            init_mem[i] = int(x)
            
    return init_mem

def execute(mem, pc=0, relative_base = 0):
    count = 0
    output = list()
    state = dict()
    state[-1,0]=0
    paddle = (0,0)
    ball = (0,0)
    score=0
    
    
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
            if (paddle[0] < ball[0]):
                val = 'r'
            elif (paddle[0] == ball[0]):
                val = 'n'
            else:
                val = 'l'
            #print(f"Moving {val}")
            #time.sleep(.1)
            
            
             #val = input(">>")
            if (val == 'n'):
                val = 0
            elif (val == 'l'):
                val = -1
            elif (val == 'r'):
                val = 1
                
            if param_mode[2] == "2":
                #print(f"Setting pos {mem[pc+1]}+{relative_base} to {val}")
                mem[mem[pc+1]+relative_base] = val
            else:
                #print(f"Setting pos {mem[pc+1]} to {val}")
                mem[mem[pc+1]] = val

        elif opcode == 4:
            #print(f"Outputting {r[0]}")
            #print(r[0])
            output.append(r[0])

            if len(output) == 3:
                if output[0] == -1 and output[1] == 0:
                    state[(-1, 0)] += 1
                    if (state[(-1, 0)] %3 == 0):
                        score = output[2]

                if output[2] == 3:
                    paddle = (output[0], output[1])
                elif output[2] == 4:
                    ball = (output[0], output[1])
                        
                state[(output[0], output[1])] = output[2]
                output = list()
                render(state, score)


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

charmap = {0: ' ',
           1: '|',
           2: 'b',
           3: '-',
           4: 'O'}

def render(state, score):
    x_size = max([x[0] for x in state.keys()])
    y_size = max([x[1] for x in state.keys()])    

    print(y_size)
    for y in range(0, y_size):
        row = list()
        for x in range(0, x_size):
            if (x,y) in state:
                row.append(charmap[state[(x,y)]])
            else:
                row.append(' ')
        print(''.join(row))
    print(f"Score: {score}")

    
                
            
            

def main():
    mem = read_input('game_input')
    pc = 0
    rb = 0

    mem[0] = 2
    while True:
        (halt, tile, pc, rb) =  execute(mem, pc, rb)
        if halt:
            break




if __name__=='__main__':
    main()
        
        
