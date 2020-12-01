from day01 import find_pair, find_triple, find_iter

expense_report = [1721, 979, 366, 299, 675, 1456]
expense_report.sort()

def test_day01_part1():
    (x, y) = find_pair(expense_report)
    assert (x, y, x * y) == (299, 1721, 514579)

    (x, y) = find_iter(expense_report, 2)
    assert (x, y, x * y) == (299, 1721, 514579)

def test_day01_part2():
    (x, y, z) = find_triple(expense_report)
    assert (x, y, z, x * y * z) == (366, 675, 979, 241861950)

    (x, y, z) = find_iter(expense_report, 3)
    assert (x, y, z, x * y * z) == (366, 675, 979, 241861950)
