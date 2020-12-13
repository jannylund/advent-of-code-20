from timeit import default_timer as timer
from utils.time import get_time
from math import ceil


def parse_notes(notes):
    earliest = int(notes[0])
    bus_ids = list(map(int, [bus for bus in notes[1].split(",") if bus != 'x']))
    return earliest, sorted(bus_ids)


def find_earliest_bus(notes):
    earliest, bus_ids = parse_notes(notes)
    starts = {}
    for bus in bus_ids:
        starts[(ceil(earliest/bus) * bus) - earliest] = bus

    first_start = min(starts.keys())
    bus_id = starts[first_start]
    return first_start * bus_id


def parse_buses(notes):
    bus_ids = notes.split(",")
    r = {}
    for i in range(0, len(bus_ids)):
        bus = bus_ids[i]
        if bus != 'x':
            r[int(bus)] = i
    return r


def get_step(bus_ids):
    r = 1
    for b in bus_ids:
        r = r * b
    return r


def find_sequence_timestamp(bus_notes):
    bus_offsets = parse_buses(bus_notes)

    # loop around the _largest_ bus_id to minimize amount of loops.
    bus_ids = list(bus_offsets.keys())
    target_bus = bus_ids[0]

    bus_ids = sorted(bus_ids)
    bus_ids.reverse()

    time = 0

    # contain a list of buses we found matches for.
    step_buses = [target_bus]
    is_valid = False
    while not is_valid:
        is_valid = True # think positive!
        step = get_step(step_buses)
        time = time + step
        for bus_id in bus_ids:
            bus_t = time + bus_offsets[bus_id]
            if bus_t % bus_id == 0:
                if bus_id not in step_buses:
                    step_buses.append(bus_id)
            else:
                is_valid = False
                break
        if is_valid:
            break
    return time


if __name__ == "__main__":
    with open('input/day13.txt') as f:
        notes = f.read().splitlines()

    start = timer()
    print("result day 13 part 1: {} in {}".format(find_earliest_bus(notes), get_time(start)))

    start = timer()
    print("result day 13 part 2: {} in {}".format(find_sequence_timestamp(notes[1]), get_time(start)))
