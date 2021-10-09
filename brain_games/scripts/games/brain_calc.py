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
        quesiton_str = (str(number1)
                        + " "
                        + str(dict_math_oper[number_math_oper])
                        + " "
                        + str(number2))

        vie.print_question(quesiton_str)
        user_answer = vie.get_user_answer().strip()
        correct_answer = get_correct_answer(quesiton_str)
        print('a: ', type(user_answer))

        if correct_answer == int(user_answer):
            vie.correct_answer()
            print(user_answer, "!!!")
        else:
            vie.wrong_answer(name, user_answer, correct_answer)
            print(user_answer, "!!!")
            sys.exit()


def get_correct_answer(_str):
    return eval(_str)


if __name__ == '__main__':
    main()
