from day05 import *

def test_day05_part1():
    assert check_boardingpass("FBFBBFFRLR") == (44, 5, 357)
    assert check_boardingpass("BFFFBBFRRR") == (70, 7, 567)
    assert check_boardingpass("FFFBBBFRRR") == (14, 7, 119)
    assert check_boardingpass("BBFFBBFRLL") == (102, 4, 820)
