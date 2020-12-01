#!/usr/bin/env python3

def fuel(mass):
    return int(mass/3) - 2

def main():
    module_mass = list()
    total_fuel = 0

    with open('game_input', 'r') as f:
        for line in f:
            module_mass.append(int(line.rstrip()))


    fuel_count = [fuel(m) for m in module_mass]

    print(f"Fuel for Mass {sum(fuel_count)}")

    total_fuel = 0
    for mass in module_mass:
        module_fuel = fuel(mass)

        next_fuel = module_fuel
        while True:
            new_fuel = fuel(next_fuel)
            next_fuel = new_fuel
            if next_fuel < 0:
                break
            module_fuel += new_fuel

        total_fuel += module_fuel

    print (f"Total Fuel {total_fuel}")

if __name__ == '__main__':
    main()