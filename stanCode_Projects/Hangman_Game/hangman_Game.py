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

    word = random_word()
    dashed = word_in_dashed(word)
    word_guess(word, dashed)


def word_in_dashed(word):
    # The vocabulary will be shown by dash before guess.
    dashed = ''
    for i in range(len(word)):
        dashed += '-'
    print('The word looks like: ' + dashed)
    print('You have ' + str(N_TURNS) + ' guesses left')
    return dashed


def word_guess(w, d):
    
    count = N_TURNS
    while True:
        your_guess = input('Your guess: ').upper()
        if not your_guess.isalpha() or len(your_guess) != 1:
            print('Illegal format.')
        else:
            answer = ''
            if your_guess in w:
                for j in range(len(d)):
                    if w[j] == your_guess:
                        answer += your_guess
                    else:
                        answer += d[j]
                d = answer
                print('You are correct!')
                if w == d:
                    print('You are win!')
                    print('The word was: ' + d)
                    break
                else:
                    print('The word looks like: ' + d)
                    print('You have ' + str(count) + ' guesses left')
            else:
                count -= 1
                print('There is no \'' + your_guess + '\' in word.')
                if count == 0:
                    print('You are completely hung :(')
                    print('The word was: ' + w)
                    break
                else:
                    print('The word looks like: ' + d)
                    print('You have ' + str(count) + ' guesses left')


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
