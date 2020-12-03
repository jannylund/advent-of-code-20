from timeit import default_timer as timer
from utils.time import get_time

TREE="#"


def count_trees(geo, curr_x=0, curr_y=0, acc=0, slope_x=3, slope_y=1):
    max_x = len(geo[0])
    max_y = len(geo)

    if curr_y >= max_y:
        return acc

    if geo[curr_y][curr_x % max_x] == TREE:
        acc += 1

    return count_trees(geo, curr_x + slope_x, curr_y + slope_y, acc, slope_x, slope_y)


if __name__ == "__main__":
    with open('input/day03.txt') as f:
        geo = f.read().splitlines()

    start = timer()
    print("result day 03 part 1: {} in {}".format(count_trees(geo), get_time(start)))

    start = timer()
    slope_1 = count_trees(geo, slope_x=1, slope_y=1)
    slope_2 = count_trees(geo, slope_x=3, slope_y=1)
    slope_3 = count_trees(geo, slope_x=5, slope_y=1)
    slope_4 = count_trees(geo, slope_x=7, slope_y=1)
    slope_5 = count_trees(geo, slope_x=1, slope_y=2)

    print("result day 03 part 2: {} in {}".format((slope_1 * slope_2 * slope_3 * slope_4 * slope_5), get_time(start)))
