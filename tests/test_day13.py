from day13 import *


notes="""939
7,13,x,x,59,x,31,19""".splitlines()


def test_day13_part1():

    earliest, buses = parse_notes(notes)
    assert earliest == 939
    assert buses == [7, 13, 19, 31, 59]
    assert find_earliest_bus(notes) == 295


def test_day13_part2():
    assert find_sequence_timestamp("17,x,13,19") == 3417
    assert find_sequence_timestamp(notes[1]) == 1068781
    assert find_sequence_timestamp("67,7,59,61") == 754018
    assert find_sequence_timestamp("67,x,7,59,61") == 779210
    assert find_sequence_timestamp("67,7,x,59,61") == 1261476
    assert find_sequence_timestamp("1789,37,47,1889") == 1202161486
