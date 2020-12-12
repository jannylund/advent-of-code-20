from day12 import *


nav_instructions="""F10
N3
F7
R90
F11""".splitlines()



def test_day12_part1():
    assert len(nav_instructions) == 5

    assert turn('N', 'L', 0) == 'N'
    assert turn('N', 'R', 180) == 'S'
    assert turn('N', 'R', 360) == 'N'

    assert navigate(nav_instructions) == ('S', -8, 17)
    assert distance(nav_instructions) == 25


def test_day12_part2():
    assert distance_waypoint(nav_instructions) == 286
    assert turn_waypoint((4, 10), 'R', 90) == (-10, 4)
    assert turn_waypoint((-10, 4), 'R', 90) == (-4, -10)
    assert turn_waypoint((-10, 4), 'R', 90) == (-4, -10)
    assert turn_waypoint((4, 10), 'R', 360) == (4, 10)
