#!/usr/bin/env/ python

import prompt


def welcome_player():
    print('welcome to the Brain Games')


def get_name():
    return prompt.string('May I have your name? ')


def get_user_answer():
    return prompt.string('You answer: ')


def hello_player(name):
    print('Hello, {}'.format(name))


def correct_answer():
    print('Correct!')


def wrong_answer(name, user_answer, correct_answer):
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'"
          .format(user_answer, correct_answer,))
    print("Let's try again, {}".format(name))


def print_answer(question_1, question_2):
    print('Answer "{}" if the number is even, otherwise answer "{}"'
          .format(question_1, question_2))


def print_question(number):
    print('{}: {}'.format('Question', number))


def win(name):
    print('{} {}'.format('Congratulations, ', name))
