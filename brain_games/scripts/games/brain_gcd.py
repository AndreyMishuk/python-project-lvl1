#!/usr/bin/env/ python

import random
from math import gcd
from brain_games.scripts import vie
from brain_games.scripts import helper


def main():

    name = helper.greeting(
        'Find the greatest common divisor of given numbers.'
    )

    for i in range(3):
        number1 = random.randint(1, 75)
        number2 = random.randint(1, 75)
        queistion_str = (str(number1)
                         + " "
                         + str(number2))
        vie.print_question(queistion_str)
        user_answer = vie.get_user_answer().strip()
        correct_answer = get_correct_answer(queistion_str)

        if not helper.chek_correct_answer(name,
                                          int(user_answer),
                                          correct_answer):
            break
    else:
        vie.win(name)


def get_correct_answer(_str):
    len_int = [int(i) for i in _str.split()]
    return gcd(len_int[0], len_int[1])


if __name__ == '__main__':
    main()
