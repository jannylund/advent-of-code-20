from timeit import default_timer as timer
from utils.time import get_time


def check_boardingpass(code):
    code = code.replace('F', 'L') # always use L for Lower.
    row = get_pos(code[:7], lim_min=0, lim_max=127)
    col = get_pos(code[-3:], lim_min=0, lim_max=7)
    return (row, col, int(row * 8 + col))


def get_pos(row, lim_min=0, lim_max=127):
    char = row[0]
    if len(row) == 1:
        if char == 'L':
            return lim_min
        else:
            return lim_max

    step = (lim_max + 1 - lim_min) / 2
    if char == 'L':
        return get_pos(row[1:], lim_min, lim_max - step)
    else:
        return get_pos(row[1:], lim_min + step, lim_max)


def get_seat_id(seat_ids):
    for seat_id in range(min(seat_ids), max(seat_ids)):
        if not seat_id in seat_ids:
            return seat_id

if __name__ == "__main__":
    with open('input/day05.txt') as f:
        boarding_passes = f.read().splitlines()

    start = timer()
    checked_passes = [check_boardingpass(bp) for bp in boarding_passes]
    seat_ids = set([seat_id for (row, col, seat_id) in checked_passes])
    print("result day 05 part 1: {} in {}".format(max(seat_ids), get_time(start)))

    start = timer()
    print("result day 05 part 2: {} in {}".format(get_seat_id(seat_ids), get_time(start)))
