from day02 import parse_password, is_valid, valid_passwords, is_valid_toboggan, valid_passwords_toboggan

password_database = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

passwords = [parse_password(p) for p in password_database.splitlines()]

def test_day02_part1():
    assert len(passwords) == 3
    assert is_valid(passwords[0]) == True
    assert is_valid(passwords[1]) == False
    assert is_valid(passwords[2]) == True
    assert valid_passwords(passwords) == 2


def test_day02_part2():
    assert is_valid_toboggan(passwords[0]) == True
    assert is_valid_toboggan(passwords[1]) == False
    assert is_valid_toboggan(passwords[2]) == False
    assert valid_passwords_toboggan(passwords) == 1
