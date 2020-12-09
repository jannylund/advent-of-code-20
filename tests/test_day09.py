from day09 import *

example=list(map(int, """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()))


def test_day09_part1():
    assert find_first(example, 5) == 127


def test_day09_part2():
    assert find_contigous(example, 127) == 62
