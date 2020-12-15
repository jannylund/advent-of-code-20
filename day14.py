from timeit import default_timer as timer
from utils.time import get_time
import re

RE_MEM_LINE=re.compile(r"^mem\[(\d+)\]$")

def dec2bin(dec: int) -> str:
    return format(dec, '036b')

def bin2dec(bin: str) -> int:
    return int(bin, 2)


def mask_bin(bin: str, mask: str) -> str:
    b = list(bin)
    m = list(mask)

    for i in range(0, len(m)):
        if m[i] != 'X':
            b[i] = m[i]
    return "".join(b)

def mask_dec(dec: int, mask: str) -> int:
    #print("dec: '{}',  mask: '{}'".format(dec, mask))
    return bin2dec(mask_bin(dec2bin(dec), mask))


def mask_mem(dec: int, mask: str) -> int:
    b = list(dec2bin(dec))
    m = list(mask)
    for i in range(0, len(m)):
        if m[i] != '0':
            b[i] = m[i]

    # generate all memory references.
    mem = []
    x = "".join(['1' for i in range(0, b.count("X"))])
    for i in range(0, int(x, 2) + 1):
        bin_format = "0{}b".format(len(x))
        replacement = list(format(i, bin_format))
        y = "".join(b)
        for r in replacement:
            y = y.replace('X', r, 1)
        mem.append(bin2dec(y))
    return mem


def run_program(program: str) -> int:
    mask = None
    mem = {}
    for line in program:
        target, value = line.split(" = ")
        if target == 'mask':
            mask = value
        else:
            row = int(RE_MEM_LINE.findall(target)[0])
            mem[row] = mask_dec(int(value), mask)
    return sum(mem.values())


def run_mad(program: str) -> int:
    mask = None
    mem = {}
    for line in program:
        target, value = line.split(" = ")
        if target == 'mask':
            mask = value
        else:
            row = int(RE_MEM_LINE.findall(target)[0])
            addresses = mask_mem(int(row), mask)
            for address in addresses:
                mem[address] = int(value)
    return sum(mem.values())


if __name__ == "__main__":
    with open('input/day14.txt') as f:
        program = f.read().splitlines()

    start = timer()
    print("result day 14 part 1: {} in {}".format(run_program(program), get_time(start)))

    start = timer()
    print("result day 14 part 2: {} in {}".format(run_mad(program), get_time(start)))
