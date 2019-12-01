from pathlib import Path

def calc_fuel_for_mass(mass: int):
    """
        fuel required is is mass divided by 3, rounded down, minus 2
    """
    return (mass // 3) - 2


def calc_true_fuel_for_mass(mass: int):
    """
        includes the mass of the fuel itself in the calculation
    """
    additional_mass = calc_fuel_for_mass(mass)
    if additional_mass < 0:
        return 0
    else:
        return additional_mass + calc_true_fuel_for_mass(additional_mass)


def solve_part1(all_masses):
    return sum([calc_fuel_for_mass(each_mass) for each_mass in all_masses])

def solve_part2(all_masses):
    return sum([calc_true_fuel_for_mass(each_mass) for each_mass in all_masses])

if __name__ == '__main__':
    
    puzzle_input = Path.joinpath(Path(__file__).parent.absolute(),"input.txt")
    with open(puzzle_input) as file:
        masses = [int(line.strip()) for line in file]

    print(solve_part1(masses))
    print(solve_part2(masses))
