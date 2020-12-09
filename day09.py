from timeit import default_timer as timer
from utils.time import get_time
from itertools import combinations


def find_first(numbers, preamble):
    for pos in range(len(numbers)):
        if pos > preamble - 1:
            number = numbers[pos]
            prev = numbers[pos - preamble : pos]
            previous_sums = [sum(a) for a in combinations(prev, 2)]
            if number not in previous_sums:
                return number


def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def find_contigous(numbers, target):
    for i in range(2, len(numbers) -1):
        for offset in range(0, i):
            sets = chunk_list(numbers[offset:], i)
            for s in sets:
                if len(s) > 1:
                    if sum(s) == target:
                        return min(s) + max(s)


if __name__ == "__main__":
    with open('input/day09.txt') as f:
        numbers = f.read().splitlines()

    numbers = list(map(int, numbers))

    start = timer()
    target = find_first(numbers, 25)
    print("result day 09 part 1: {} in {}".format(target, get_time(start)))


    start = timer()
    print("result day 09 part 2: {} in {}".format(find_contigous(numbers, target), get_time(start)))
