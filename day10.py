from timeit import default_timer as timer
from utils.time import get_time
from itertools import combinations


def max_rating(adapters):
    return max(adapters) + 3


def find_jolt_differences(adapters):
    rs = adapters.copy()
    rs.append(0)
    rs.append(max_rating(adapters))
    rs.sort()
    differences = {}
    for r in range(1, len(rs)):
        diff = rs[r] - rs[r-1]
        if diff in differences:
            differences[diff] += 1
        else:
            differences[diff] = 1
    return differences


def find_jolt_product(adapters):
    diffs = find_jolt_differences(adapters)
    return diffs[1] * diffs[3]


# Check if adapter range is valid.
def is_valid(adapters):
    for r in range(1, len(adapters)):
        if adapters[r] - adapters[r-1] > 3:
            return False
    return True


def _count_arrangments(adapters):
    if len(adapters) < 3:
        return 1

    arr_count = 0
    a_min = min(adapters)
    a_max = max(adapters)
    for i in range(2, len(adapters) + 1):
        for a in combinations(adapters, i):
            if a_min in a and a_max in a: # we need both min and max.
                if is_valid(a):
                    arr_count += 1
    return arr_count


# split arrangments in groups that have the max jolt diff 3
def split_arrangments(adapters):
    groups = {}
    step = 0
    for i in range(0, len(adapters)):
        if adapters[i] - adapters[i-1] > 2:
            step += 1
        if step not in groups:
            groups[step] = [adapters[i]]
        else:
            groups[step].append(adapters[i])
    return [group for _, group in groups.items()]


def count_arrangements(adapters):
    adapters.append(0)
    adapters.append(max_rating(adapters))
    adapters.sort()

    combinations = 1
    for group in split_arrangments(adapters):
        combinations = combinations * _count_arrangments(group)
    return combinations


if __name__ == "__main__":
    with open('input/day10.txt') as f:
        adapters = f.read().splitlines()
    adapters = list(map(int, adapters))


    start = timer()
    print("result day 10 part 1: {} in {}".format(find_jolt_product(adapters), get_time(start)))
    start = timer()
    print("result day 10 part 2: {} in {}".format(count_arrangements(adapters), get_time(start)))
