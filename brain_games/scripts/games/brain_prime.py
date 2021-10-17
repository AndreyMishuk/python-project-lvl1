#!/usr/bin/env/ python


import random
from brain_games.scripts import vie
import sys


def main():

    vie.welcome_player()
    name = vie.get_name()
    vie.hello_player(name)
    vie.print_answer(
        'Answer "yes" if given number is prime. Otherwise answer "no"')

    for i in range(3):
        number = random.randint(1, 100)
        vie.print_question(number)
        user_answer = vie.get_user_answer()
        correct_answer = is_prime(number)
        if correct_answer == user_answer:
            vie.correct_answer()
        else:
            vie.wrong_answer(name, user_answer, correct_answer)
            sys.exit()
    vie.win(name)


def is_prime(n):
    if n % 2 == 0:
        return 'no'
    temp = 3
    while temp**2 <= n and n % temp != 0:
        temp += 2
    if temp**2 > n:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    main()
