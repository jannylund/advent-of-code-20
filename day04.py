import re
from timeit import default_timer as timer
from utils.time import get_time


REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
VALID_ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def parse_passport(line):
    fields = line.replace("\n", " ").strip().split(" ")
    return dict(f.split(":") for f in fields)


def has_fields(passport):
    return all(f in passport.keys() for f in REQUIRED_FIELDS)


def p1_valid_passports(passports):
    return len([p for p in passports if has_fields(p)])


def byr(year):
    return 1920 <= int(year) <= 2002


def iyr(year):
    return 2010 <= int(year) <= 2020


def eyr(year):
    return 2020 <= int(year) <= 2030


def hgt(hgt):
    if "cm" in hgt:
        hgt_min = 150
        hgt_max = 193
    elif "in" in hgt:
        hgt_min = 59
        hgt_max = 76
    else:
        return False

    hgt = int(hgt.replace("cm", "").replace("in", ""))
    return hgt_min <= hgt <= hgt_max


def hcl(hcl):
    return re.match("^#[0-9a-f]{6}$", hcl) is not None


def ecl(ecl):
    return ecl in VALID_ECL


def pid(pid):
    return re.match("^[0-9]{9}$", pid) is not None


def p2_valid_passports(passports):
    cnt = 0
    for p in passports:
        if not has_fields(p):
            continue
        if not byr(p['byr']):
            continue
        if not iyr(p['iyr']):
            continue
        if not eyr(p['eyr']):
            continue
        if not hgt(p['hgt']):
            continue
        if not hcl(p['hcl']):
            continue
        if not ecl(p['ecl']):
            continue
        if not pid(p['pid']):
            continue
        cnt += 1
    return cnt


if __name__ == "__main__":
    with open('input/day04.txt') as f:
        passports = f.read().split("\n\n")
    passports = [parse_passport(p) for p in passports]

    start = timer()
    print("result day 04 part 1: {} in {}".format(p1_valid_passports(passports), get_time(start)))

    start = timer()
    print("result day 04 part 2: {} in {}".format(p2_valid_passports(passports), get_time(start)))
