from day06 import *

answers="""abc

a
b
c

ab
ac

a
a
a
a

b
"""

def test_day06_part1():
    answers_anyone = [parse_answer_anyone(a) for a in answers.split("\n\n")]
    assert len(answers_anyone) == 5
    assert len(answers_anyone[0]) == 3
    assert len(answers_anyone[1]) == 3
    assert len(answers_anyone[2]) == 3
    assert len(answers_anyone[3]) == 1
    assert len(answers_anyone[4]) == 1
    assert count_sums(answers_anyone) == 11


def test_day06_part2():
    answers_everyone = [parse_answer_everyone(a) for a in answers.split("\n\n")]
    assert len(answers_everyone) == 5
    assert len(answers_everyone[0]) == 3
    assert len(answers_everyone[1]) == 0
    assert len(answers_everyone[2]) == 1
    assert len(answers_everyone[3]) == 1
    assert len(answers_everyone[4]) == 1
    assert count_sums(answers_everyone) == 6
