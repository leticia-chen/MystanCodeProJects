"""
File: hangman.py
Name: Leticia Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
User can guess it within limited times.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Program will give user a word and each letter will be in dashed,
    User has to guess which letters they are in limited times.
    """
    # The vocabulary will be shown by dash before guess.
    answer = random_word()
    dashed = ""
    for i in range(len(answer)):
        dashed += '-'
    print('The word looks like: ' + dashed)
    print('You have ' + str(N_TURNS) + ' guesses left')

    x = N_TURNS
    while True:
        # Guess all letters
        if dashed == answer:
            print('You are win!')
            print('The word was: ' + answer)
            break

        # Game over and did not guess all letters
        elif x == 0:
            print('You are completely hung :(')
            print('The word was: ' + answer)
            break

        else:
            # When typing letters in illegal format
            your_guess = input('Your guess: ')
            if not your_guess.isalpha() or len(your_guess) != 1:
                print('Illegal format.')

            else:
                your_guess = your_guess.upper()
                ch = ''
                if your_guess in answer:
                    print('You are correct!')
                    for i in range(len(answer)):
                        if your_guess == answer[i]:
                            ch += answer[i]
                        else:
                            ch += dashed[i]             # dashed string will replace ch string to keep letters guessed
                    dashed = ch
                    print('The word looks like: ' + dashed)
                    print('You have ' + str(x) + ' guesses left')
                else:
                    # if not guessing letter will lose um chance
                    x -= 1
                    print('There is no \'' + your_guess + '\' in word.')
                    print('The word looks like: ' + dashed)
                    print('You have ' + str(x) + ' guesses left')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
