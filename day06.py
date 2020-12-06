from timeit import default_timer as timer
from utils.time import get_time


def parse_answer_anyone(answer):
    return set(answer.replace("\n", "").strip())


def parse_answer_everyone(answer):
    everyone = len(answer.splitlines())
    chars = answer.replace("\n", "").strip()
    return [c for c in set(chars) if chars.count(c) == everyone]


def count_sums(answers):
    return sum([len(a) for a in answers])


if __name__ == "__main__":
    with open('input/day06.txt') as f:
        answers = f.read().split("\n\n")

    start = timer()
    answers_anyone = [parse_answer_anyone(a) for a in answers]
    print("result day 06 part 1: {} in {}".format(count_sums(answers_anyone), get_time(start)))

    start = timer()
    answers_everyone = [parse_answer_everyone(a) for a in answers]
    print("result day 06 part 2: {} in {}".format(count_sums(answers_everyone), get_time(start)))
