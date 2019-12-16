#!/usr/bin/env python3
# Part 1 was a trap, ignore everything from that code in solving part2
# - massively misread the problem prompt, thought the message offset was taken from the final output. Oy
# - needed some biiiig hints (and copying from solved sources) from reddit here...

# This code takes wayyy to long.

def phase(inp):
    line = list()

    # We've already skipped every element < msg_offset (as its pattern is 0)
    # Now, given how large msg_offset is, every elem from here on out is *
    # with a pattern of 1 (the other pattern 0's and -1s fall off the end of
    # of the input
    for i in range(len(inp)):
        line.append(sum(inp[i:]) % 10)
        
    return line
            
def main():
    out = [int(x) for x in open('game_input', 'r').read().rstrip()]

    msg_offset = int(''.join([str(x) for x in out[0:7]]))
    print("Message offset:", msg_offset)    

    #BP Answer: part 2: 84024125

    # Skip everything prior to the message offset, since it will be 0'd out from leading zeros in the pattern    
    out = out * 10000
    out = out[msg_offset:]

    phases = 100
    for i in range(0, phases):
        print(i)
        
        out = phase(out)

    print(''.join([str(x) for x in out[0:8]]))


        

if __name__ == '__main__':
    main()
