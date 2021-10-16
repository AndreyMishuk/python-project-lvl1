#!/usr/bin/env/ python

import random
from brain_games.scripts import vie
import sys


def main():
    vie.welcome_player()
    name = vie.get_name()
    vie.hello_player(name)

    vie.print_answer(
        'Answer "yes" if the number is even, otherwise answer "no"')
    for i in range(3):
        number = random.randint(1, 100)
        vie.print_question(number)
        user_answer = vie.get_user_answer()
        correct_answer = get_correct_answer(number)
        if correct_answer == user_answer:
            vie.correct_answer()
        else:
            vie.wrong_answer(name, user_answer, correct_answer)
            sys.exit()
    vie.win(name)


def get_correct_answer(numb):
    return 'yes' if numb % 2 == 0 else 'no'


if __name__ == '__main__':
    main()
