from timeit import default_timer as timer
from utils.time import get_time


def find_pair(arr, sum=2020):
    for x in arr:
        for y in arr:
            if x is not y and x + y == sum:
                return (x, y)


def find_triple(arr, sum=2020):
    for x in arr:
        pair = find_pair(arr, sum - x)
        if pair is not None and x not in pair:
            (y, z) = pair
            if (x + y + z) == sum:
                return (x, y, z)


if __name__ == "__main__":
    with open('input/day01.txt') as f:
        expense_report = [int(m) for m in f.read().splitlines()]
    expense_report.sort()

    start = timer()
    (x, y) = find_pair(expense_report)
    print("result day 01 part 1: pair={}, product={} in {}".format((x, y), x * y, get_time(start)))

    start = timer()
    (x, y, z) = find_triple(expense_report)
    print("result day 01 part 2: triple={}, product={} in {}".format((x, y, z), x * y * z, get_time(start)))
