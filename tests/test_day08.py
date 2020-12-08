from day08 import *


instructions="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()



def test_day08_part1():
    program = parse_instructions(instructions)
    result, normal_exit = run(program)
    assert result == 5


def test_day08_part2():
    program = parse_instructions(instructions)
    assert run_fixed(program) == 8
