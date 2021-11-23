#!/usr/bin/env/ python


import random
from brain_games.scripts import vie
from brain_games.scripts import helper


def main():

    name = 1
#    name = helper.greeting(
#        'Answer "yes" if given number is prime. Otherwise answer "no"'
#    )

    for i in range(3):
        number = random.randint(1, 100)
        vie.print_question(number)
        user_answer = vie.get_user_answer()
        correct_answer = is_prime(number)

        if not helper.chek_correct_answer(name, user_answer, correct_answer):
            break
    else:
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
