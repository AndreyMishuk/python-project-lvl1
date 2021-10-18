#!/usr/bin/env/ python


import random
from brain_games.scripts import vie
from brain_games.scripts import helper


def main():

    dict_math_oper = {1: '+', 2: '-', 3: '*'}

    name = helper.greeting('What is the result of the expression?')

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

        if not helper.chek_correct_answer(name,
                                          int(user_answer),
                                          correct_answer):
            break
    else:
        vie.win(name)


def get_correct_answer(_str):
    return eval(_str)


if __name__ == '__main__':
    main()
