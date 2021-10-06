#!/usr/bin/env/ python


import sys
import random
from brain_games.scripts import vie


def main():

    vie.welcome_player()
    name = vie.get_name()
    vie.hello_player(name)

    dict_math_oper = {1: '+', 2: '-', 3: '*'}

    vie.print_answer('What is the result of the expression?')

    for i in range(3):

        number1 = random.randint(1, 50)
        number2 = random.randint(1, 25)
        number_math_oper = random.randint(1, 3)
        qustion_str = str(number1)
        + " "
        + str(dict_math_oper[number_math_oper])
        + " "
        + str(number2)

        vie.print_question(qustion_str)
        user_answer = vie.get_user_answer()


if __name__ == '__main__':
    main()
