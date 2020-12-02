from timeit import default_timer as timer
from utils.time import get_time

def parse_password(line):
    char_min, char_max, char, password = line.replace("-", " ").replace(":", "").split(" ")
    return (int(char_min), int(char_max), char, password)


def is_valid(password):
    char_min, char_max, char, password = password
    char_curr = password.count(char)
    return char_min <= char_curr and char_max >= char_curr


def valid_passwords(passwords):
    return len([p for p in passwords if is_valid(p)])


def is_valid_toboggan(password):
    pos_1, pos_2, char, password = password
    return (password[pos_1 - 1] == char) != (password[pos_2 - 1] == char)


def valid_passwords_toboggan(passwords):
    return len([p for p in passwords if is_valid_toboggan(p)])


if __name__ == "__main__":
    with open('input/day02.txt') as f:
        passwords = [parse_password(p) for p in f.read().splitlines()]

    start = timer()
    print("result day 02 part 1: {} in {}".format(valid_passwords(passwords), get_time(start)))

    start = timer()
    print("result day 02 part 2: {} in {}".format(valid_passwords_toboggan(passwords), get_time(start)))
