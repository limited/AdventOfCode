#!/usr/bin/env python3

# Start 8:00, snowblowed until 9ish
# Part1: 9:27
# Part2: 10:45, wasted about an hour figuring out that I was rendering all pixels as white regardless of value



move_dict = { 'u': (0, 1),
              'd': (0, -1),
              'l': (-1, 0),
              'r': (1,  0)
              }

next_face = {'u': {0: 'l', 1: 'r'},
             'd': {0: 'r', 1: 'l'},
             'l': {0: 'd', 1: 'u'},
             'r': {0: 'u', 1: 'd'}}
         

def read_input(name):
    init_mem = [0 for x in range(0,5000000)]
    
    with open(name, 'r') as f:
        pinput = f.readline().rstrip()
        for i, x in enumerate(pinput.split(',')):
            init_mem[i] = int(x)
            
    return init_mem

def input_func(hull, pos):
    if pos in hull:
        return hull[pos]
    else:
        return 0

def execute(mem, hull, pos, pc=0, relative_base = 0):
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
            #val = int(input(">>"))
            val = int(input_func(hull, pos))
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
            break

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

def main():
    mem = read_input('game_input')
    pos = (0,0)
    hull = dict()
    pc = 0
    rb = 0

    # Emergency Hull Painting Robot Starting Panel
    hull[pos] = 1

    facing = 'l'
    try:
        while True:
            (halt, color, pc, rb) =  execute(mem, hull, pos, pc, rb)
            if halt:
                print("--------HALT---------")
                break
            hull[pos] = color
            print(f"Painting {pos} to {color}")
        
            (halt, turn, pc, rb) = execute(mem, hull, pos, pc, rb)
            if halt:
                
                print(f"Painted {len(hull.keys())} panels")
                break

            #print(f"Was facing {facing}")
            facing = next_face[facing][turn]
            print(f"Turning {turn} now facing {facing}")# at {pos}" )
            pos = (pos[0] + move_dict[facing][0] ,pos[1]+move_dict[facing][1])
            print(f"Moving to {pos}")
            #print("-----")
                      
    except KeyError:
        print("KeyError")
        return

    print(len(hull))
    print(hull)
        
    size = 256
    from PIL import Image
    img = Image.new('RGB', (size, size), "black")
    pixels = img.load()
    center = size/2
    print(type(hull))
    for p in hull:
        if hull[p] == 1:    
            pixels[p[0]+center, p[1]+center] = (255, 255, 255)
    img.show()

if __name__ == '__main__':
    main()
