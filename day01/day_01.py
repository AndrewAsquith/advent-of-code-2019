from pathlib import Path

def calc_fuel_for_mass(mass: int):
    return (mass // 3) - 2


def solve_part1(all_masses):
    return sum([calc_fuel_for_mass(each_mass) for each_mass in all_masses])


if __name__ == '__main__':
    
    with Path.joinpath(Path(__file__).parent.absolute(),"input.txt").open() as file:
        masses = [int(line.strip()) for line in file]

    print(solve_part1(masses))
