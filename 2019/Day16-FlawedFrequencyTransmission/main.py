#!/usr/bin/env python3

base_pattern = [0, 1, 0, -1]
def pattern(position, repeats):
    return base_pattern[(position//repeats) % len(base_pattern)]

def main():
    out = [int(x) for x in open('game_input', 'r').read().rstrip()]
    #print(out)


    newl = list()

    #    for j in range(0, len(out)):
    #        print(out[j], pattern(j+1, 0+1), out[j]*pattern(j+1, 0+1))
    #        newl.append(out[j]*pattern(j+1, 0+1))
    #print(abs(sum(newl))%10)

    phases = 100   
    for p in range(0, phases):
        print(p)
        out = [abs(sum([out[j] * pattern(j+1, idx+1) for j in range(0, len(out))])) % 10 for idx, i in enumerate(out)]
        #print(out)

    print(out[0:8])
        

if __name__ == '__main__':
    main()
