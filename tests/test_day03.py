from day03 import count_trees

geo = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()


def test_day03_part1():
    assert count_trees(geo) == 7


def test_day03_part2():
    slope_1 = count_trees(geo, slope_x=1, slope_y=1)
    slope_2 = count_trees(geo, slope_x=3, slope_y=1)
    slope_3 = count_trees(geo, slope_x=5, slope_y=1)
    slope_4 = count_trees(geo, slope_x=7, slope_y=1)
    slope_5 = count_trees(geo, slope_x=1, slope_y=2)
    assert slope_1 == 2
    assert slope_2 == 7
    assert slope_3 == 3
    assert slope_4 == 4
    assert slope_5 == 2

    assert (slope_1 * slope_2 * slope_3 * slope_4 * slope_5) == 336



