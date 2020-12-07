import re
from timeit import default_timer as timer
from utils.time import get_time


NO_OTHER="no other"
RE_CNT_COLOR=re.compile(r"(\d)? ?(\w* \w*) bag")

# use a global as cache.
cache = {}


def build_tree(rules):
    tree = {}
    for r in rules:
        colors = [(color, count) for count, color in RE_CNT_COLOR.findall(r) if not color == NO_OTHER]
        tree[colors[0][0]] = colors[1:]
    return tree


def get_carrier(tree, color):
    global cache
    bags = []
    for bag in tree:
        if color in tree[bag]:
            if not bag in cache:
                cache[bag] = get_carrier(tree, bag)
            bags.extend([bag] + cache[bag])
    return list(set(bags))


def can_carry(tree, color="shiny gold"):
    # simplify the tree to a color tree for speed.
    color_tree = {}
    for bag in tree:
        color_tree[bag] = [color for color, count in tree[bag]]
    return set(get_carrier(color_tree, color))


def count_children(tree, color):
    cnt = 1
    for child_color, count in tree[color]:
        cnt += int(count) * count_children(tree, child_color)
    return cnt


if __name__ == "__main__":
    with open('input/day07.txt') as f:
        rules = f.read().splitlines()

    start = timer()
    tree = build_tree(rules)
    print("result day 07 part 1: {} in {}".format(len(can_carry(tree, "shiny gold")), get_time(start)))

    start = timer()
    print("result day 07 part 2: {} in {}".format(count_children(tree, "shiny gold") - 1, get_time(start)))
