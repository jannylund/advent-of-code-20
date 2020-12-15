from day14 import *


program="""mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".splitlines()


def test_day14_part1():
    assert dec2bin(11) == "000000000000000000000000000000001011"
    assert bin2dec("000000000000000000000000000000001011") == 11

    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    assert mask_bin("000000000000000000000000000000001011", mask) == "000000000000000000000000000001001001"
    assert mask_dec(11, mask) == 73
    assert mask_dec(101, mask) == 101
    assert mask_dec(0, mask) == 64
    assert run_program(program) == 165

    assert mask_dec(2508973, "X00X0X0110010001010X0000000010001111") == 420741263


def test_day14_part2():
    #assert mask_mem(42, "000000000000000000000000000000X1001X") == "000000000000000000000000000000X1101X"

    p = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".splitlines()
    assert run_mad(p) == 208
