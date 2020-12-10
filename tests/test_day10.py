from day10 import *

adapters="""16
10
15
5
1
11
7
19
6
12
4""".splitlines()
adapters = list(map(int, adapters))


adapters_2="""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".splitlines()
adapters_2 = list(map(int, adapters_2))


def test_day10_part1():
    assert max_rating(adapters) == 22
    assert find_jolt_differences(adapters) == {1: 7, 3: 5}
    assert find_jolt_differences(adapters_2) == {1: 22, 3: 10}
    assert find_jolt_product(adapters_2) == 220



def test_day10_part2():
    assert count_arrangements(adapters) == 8
    assert count_arrangements(adapters_2) == 19208
