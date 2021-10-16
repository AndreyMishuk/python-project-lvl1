#!/usr/bin/env/ python

import random
import sys
from math import gcd
from brain_games.scripts import vie


def main():
    vie.welcome_player()
    name = vie.get_name()
    vie.hello_player(name)

    vie.print_answer('Find the greatest common divisor of given numbers.')

    for i in range(3):
        number1 = random.randint(1, 75)
        number2 = random.randint(1, 75)
        queistion_str = (str(number1)
                         + " "
                         + number2)
        vie.print_question(queistion_str)
        user_answer = vie.get_user_answer().strip()
        correct_answer = get_correct_answer(queistion_str)

        if correct_answer == int(user_answer):
            vie.correct_answer()
        else:
            vie.wrong_answer(name, user_answer, correct_answer)
            sys.exit()
    vie.win(name)


def get_correct_answer(_str):
    len_int = [int(i) for i in _str.split()]
    return gcd(len_int[0], len_int[1])


if __name__ == '__main__':
    main()
