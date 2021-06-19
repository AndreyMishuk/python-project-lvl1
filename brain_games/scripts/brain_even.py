#!/usr/bin/env/ python

import sys
import random
import prompt
import brain_games.scripts.brain_games as brain


def main():
    brain.main()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    for i in range(3):
        number = random.randint(1, 100)
        print('{} {}'.format('Question:', number))
        user_answer = prompt.string('Your answer: ')
        correct_answer = check_correct_answer(number)
        if correct_answer == user_answer:
            print('Correct!')
        else:
            end_game(user_answer, correct_answer)
    print('{} {}'.format('Congratulations, ', brain.NAME))


def check_correct_answer(numb):
    return 'yes' if numb % 2 == 0 else 'no'


def end_game(user_answer, correct_answer):
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'".
          format(user_answer, correct_answer,))
    print("Let's try again, {}".format(brain.NAME))
    sys.exit()


if __name__ == '__main__':
    main()
