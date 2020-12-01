#!/usr/bin/env python3

import sys

def read_input():
    with open('game_input', 'r') as f:
        input = f.readline().rstrip()
        return [int(x) for x in input.split(',')]


def preprocess_input(input):
    input[1] = 12
    input[2] = 2


def execute(input):
    new_start = 0
    while True:
        #print("Input", input)
        #print("Instruction Pointer", new_start)
        if input[new_start] == 99:
            break

        elif input[new_start] == 1: # ADD Opcode
            (add_idx1, add_idx2, sum_idx) = input[new_start + 1:new_start + 4]
            #print(add_idx1, add_idx2, sum_idx)
            input[sum_idx] = input[add_idx1] + input[add_idx2]
            new_start += 4

        elif input[new_start] == 2: # MULT Opcode
            #print("in", input[new_start + 1:new_start + 4])
            (mult_in1, mult_in2, mult_idx) = input[new_start+1:new_start+4]
            #print(mult_in1, mult_in2, mult_idx)
            input[mult_idx] = input[mult_in1] * input[mult_in2]
            new_start += 4

        else:
            print("INVALID OPCODE:", input[new_start])
            break

    return input[0]

def main():
    input = read_input()
    pristine_input = list(input)
    preprocess_input(input)

    # test_in = "1,9,10,3,2,3,11,0,99,30,40,50"
    # test_in = "1,0,0,0,99"
    # test_in = "2,3,0,3,99"
    # test_in = "2,4,4,5,99,0"
    # test_in = "1,1,1,4,99,5,6,0,99"
    # input = [int(x) for x in test_in.split(',')]
    answer = execute(input)
    print("Part1 Answer", answer)

    for noun in range(0, 100):
        for verb in range(0, 100):
            loop_in = list(pristine_input)
            loop_in[1] = noun
            loop_in[2] = verb
            answer = execute(loop_in)
            print(noun, verb, answer)
            if answer == 19690720:
                print(f"Noun: {noun}, Verb:{verb}")
                print(f"Result: {100 * noun + verb}")
                sys.exit(0)

if __name__ == '__main__':
    main()
