#!/usr/bin/env/ python

import random
from brain_games.scripts import vie
from brain_games.scripts import helper


def main():

    name = helper.greeting(
        'Answer "yes" if the number is even, otherwise answer "no"'
    )

    for i in range(3):
        number = random.randint(1, 100)
        vie.print_question(number)
        user_answer = vie.get_user_answer()
        correct_answer = get_correct_answer(number)

        if not helper.chek_correct_answer(name, user_answer, correct_answer):
            break
    else:
        vie.win(name)


def get_correct_answer(numb):
    return 'yes' if numb % 2 == 0 else 'no'


if __name__ == '__main__':
    main()
