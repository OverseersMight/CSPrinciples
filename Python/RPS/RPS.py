import msvcrt
import os
import random
import re


def clear(): os.system("cls")


def instructions():
    say = input("Do you wish to see the instructions?\n")
    if re.search("^ye?s?$", say):
        print("Rock beats Scissors, Scissors beats Paper, and Paper beats rock.\nPress any key to continue.")
        msvcrt.getch()
        clear()
    elif not re.search("^no?$", say):
        clear()
        instructions()
    else:
        clear()


def getRounds():
    times = int(input('How many rounds do you wish to play?\n'))
    if times > 9 or times < 1:
        clear()
        print("Invalid response, must be in the range of 1-9... Press any key to continue.")
        msvcrt.getch()
        clear()
        return getRounds()
    clear()
    return times


def playerMove():
    move = input("Do you want to choose rock, paper, or scissors?\n")
    sr = "^sc?i?s?s?o?r?s?$"  # scissors
    rr = "^ro?c?k?$"  # rock
    pr = "^pa?p?e?r?$"  # paper

    clear()

    return 1 if re.search(sr, move) else 2 if re.search(rr, move) else 3 if re.search(pr, move) \
        else playerMove(), clear()


def determineWinner(p, c):
    return "won" if p == 1 and c == 3 else "won" if p == 2 and c == 1 else "won" if p == 3 and c == 2 else "lost"


def convert(num):
    return "scissors" if num == 1 else "rock" if num == 2 else "paper"


def main():
    clear()  # Clean up any lines that were there before running the program.

    instructions()
    rounds = getRounds()

    while rounds > 0:
        rounds -= 1

        p_move = playerMove()
        c_move = random.randint(1, 3)
        if p_move == -1:
            print("Invalid move, press any key to repeat round.")
            msvcrt.getch()
            break

        print("You %s this round, as the computer chose %s and you chose %s." %
              (determineWinner(p_move, c_move), convert(c_move), convert(p_move)))
        print("Press any key to continue on to the next round.")
        msvcrt.getch()
        clear()


main()
