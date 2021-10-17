#!/usr/bin/env/ python

from brain_games.scripts import vie


def greeting(str_question):

    """greting the player and returns name player's"""

    vie.welcome_player()
    name = vie.get_name()
    vie.hello_player(name)
    vie.print_answer(str_question)

    return name


def chek_correct_answer(name, user_answer, correct_answer):

    if correct_answer == user_answer:
        vie.correct_answer()
        return True
    else:
        vie.wrong_answer(name, user_answer, correct_answer)
        return False
