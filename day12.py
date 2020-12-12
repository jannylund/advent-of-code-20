from timeit import default_timer as timer
from utils.time import get_time


def parse_instructions(instructions):
    routes = []
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        routes.append((action, value))
    return routes


def turn(direction, rotation, value):
    directions = ['N', 'E', 'S', 'W']
    step = int(value / 90) # we just support 90 degree rotations.
    curr_dir = directions.index(direction)
    if rotation == 'L':
        new_dir = (curr_dir - step) % 4
    else:
        new_dir = (curr_dir + step) % 4
    return directions[new_dir]


def move(coord, direction, value):
    x, y = coord
    if direction == 'N':
        x += value
    elif direction == 'S':
        x -= value
    elif direction == 'E':
        y += value
    elif direction == 'W':
        y -= value
    return (x, y)


def step(pos, instruction):
    direction, x, y = pos
    action, value = instruction

    if action in ['N', 'S', 'W', 'E']:
        x, y = move((x, y), action, value)
    elif action == 'F':
        x, y = move((x, y), direction, value)
    elif action in ['L', 'R']:
        direction = turn(direction, action, value)

    pos = (direction, x, y)
    return pos


def navigate(instructions):
    pos = ('E', 0, 0) # facing east, position 0, 0
    for instruction in parse_instructions(instructions):
        pos = step(pos, instruction)
    return pos


def distance(instructions):
    _, x, y = navigate(instructions)
    return abs(x) + abs(y)


def turn_waypoint(waypoint, rotation, value):
    value = value % 360
    w_x, w_y = waypoint
    if (rotation == 'R' and value == 90) or (rotation == 'L' and value == 270):
        waypoint = (-w_y, w_x)
    elif value == 180:
        waypoint = (-w_x, -w_y)
    elif (rotation == 'R' and value == 270) or (rotation == 'L' and value == 90):
        waypoint = (w_y, -w_x)
    return waypoint


def step_waypoint(pos, waypoint, instruction):
    action, value = instruction
    if action in ['N', 'S', 'W', 'E']:
        waypoint = move(waypoint, action, value)
    elif action == 'F':
        direction, x, y = pos
        w_x, w_y = waypoint
        pos = (direction, x + (value * w_x), y + (value * w_y))
    elif action in ['L', 'R']:
        waypoint = turn_waypoint(waypoint, action, value)
    return pos, waypoint


def navigate_waypoint(instructions):
    pos = ('E', 0, 0) # facing east, position 0, 0
    waypoint = (1, 10) # 1 north, 10 east
    for instruction in parse_instructions(instructions):
        pos, waypoint = step_waypoint(pos, waypoint, instruction)
    return pos


def distance_waypoint(instructions):
    _, x, y = navigate_waypoint(instructions)
    return abs(x) + abs(y)



if __name__ == "__main__":
    with open('input/day12.txt') as f:
        nav_instructions = f.read().splitlines()

    start = timer()
    print("result day 12 part 1: {} in {}".format(distance(nav_instructions), get_time(start)))

    start = timer()
    print("result day 12 part 2: {} in {}".format(distance_waypoint(nav_instructions), get_time(start)))
