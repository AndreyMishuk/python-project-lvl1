#!/usr/bin/env/ python

from brain_games.cli import welcome_user

NAME = None


def main():
    global NAME
    print('Welcome to the Brain Games!')
    NAME = welcome_user('May I have your name? ')
    print('Hello, {}'.format(NAME))


if __name__ == '__main__':
    main()
