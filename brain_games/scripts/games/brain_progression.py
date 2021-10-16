#!/usr/bin/env/ python

import random
from brain_games.scripts import vie
import sys


def main():

    vie.welcome_player()
    name = vie.get_name()
    vie.hello_player(name)
    vie.print_answer(
        'What number is missing in the progression?')

    for i in range(3):
        progression = make_progression()
        correct_answer = get_correct_answer(progression)
        question = make_str_question(progression, correct_answer)
        vie.print_question(question)
        user_answer = vie.get_user_answer()

        if correct_answer == int(user_answer):
            vie.correct_answer()
        else:
            vie.wrong_answer(name, user_answer, correct_answer)
            sys.exit()
    vie.win(name)


def make_progression():
    n1 = random.randint(1, 10)
    step = random.randint(2, 10)
    length = random.randint(5, 10)

    return [x for x in range(n1, (n1 + step * length), step)]


def make_str_question(progression, correct_answer):
    index = progression.index(correct_answer)
    progression[index] = '..'
    return ' '.join(map(str, progression))


def get_correct_answer(progression_list):
    random_number_for_question = random.randint(1, len(progression_list))
    return progression_list[random_number_for_question - 1]


if __name__ == '__main__':
    main()
