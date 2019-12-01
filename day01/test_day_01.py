import day_01
import pytest

testdata_part1 = [(12,2),(14,2),(1969,654),(100756,33583)]
testdata_part2 = [(14,2),(1969,966),(100756,50346)]

@pytest.mark.parametrize("mass,expected", testdata_part1)
def test_calc_fuel_for_mass(mass, expected):
    assert expected == day_01.calc_fuel_for_mass(mass)


@pytest.mark.parametrize("mass,expected", testdata_part2)
def test_calc_true_fuel_for_mass(mass, expected):
    assert expected == day_01.calc_true_fuel_for_mass(mass)