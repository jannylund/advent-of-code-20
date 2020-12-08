from timeit import default_timer as timer
from utils.time import get_time



def parse_instructions(instructions):
    program = []
    for instruction in instructions:
        operation, argument = instruction.split(" ")
        program.append((operation, int(argument)))
    return program


def run(program):
    acc = 0
    pos = 0
    end_pos = len(program)
    has_run = []
    while pos not in has_run and pos < end_pos:
        has_run.append(pos)
        op, arg = program[pos]
        if op == "acc":
            acc = acc + arg
            pos = pos + 1
        elif op == "jmp":
            pos = pos + arg
        elif op == "nop":
            pos = pos + 1
    return (acc, pos not in has_run)


def run_fixed(program):
    # try changing one jmp/nop at a time and run to see if it exists normally.
    normal_exit = False
    pos = 0
    result = 0
    while not normal_exit:
        op, arg = program[pos]
        new_program = program.copy()
        if op == "jmp":
            new_program[pos] = ("nop", arg)
            result, normal_exit = run(new_program)
        elif op == "nop":
            new_program[pos] = ("jmp", arg)
            result, normal_exit = run(new_program)
        pos = pos + 1
    return result


if __name__ == "__main__":
    with open('input/day08.txt') as f:
        instructions = f.read().splitlines()

    start = timer()
    program = parse_instructions(instructions)
    result, _ = run(program)
    print("result day 07 part 1: {} in {}".format(result, get_time(start)))

    start = timer()
    program = parse_instructions(instructions)
    print("result day 07 part 2: {} in {}".format(run_fixed(program), get_time(start)))
