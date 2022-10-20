import msvcrt
import os
import random
import re
import time


def clear(): os.system("cls")


def toInt(to_convert):
    try:
        return int(to_convert)
    except ValueError:
        return False


print("This program will only display correctly in Window's Command Prompt.")
time.sleep(3)


def instructions():
    say = input("Do you wish to see the instructions?\n")
    if re.search("^ye?s?$", say):
        print("Rock beats Scissors, Scissors beats Paper, and Paper beats rock.")
        time.sleep(1.75)
        clear()
        print("Press any key to continue.")
        msvcrt.getch()
        clear()
    elif not re.search("^no?$", say):
        clear()
        instructions()
    else:
        clear()


def getRounds():
    times = toInt(input('How many rounds do you wish to play?\n'))
    if times is False or times > 9 or times < 1:
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

    return 1 if re.search(sr, move) \
        else 2 if re.search(rr, move) \
        else 3 if re.search(pr, move) \
        else playerMove()


def determineWinner(p, c):
    return "tied" if p == c \
        else "won" if p == 1 and c == 3 \
        else "won" if p == 2 and c == 1 \
        else "won" if p == 3 and c == 2 \
        else "lost"


def convert(num):
    return "scissors" if num == 1 \
        else "rock" if num == 2 \
        else "paper"


def main():
    clear()  # Clean up any lines that were there before running the program.

    instructions()
    rounds = getRounds()
    player_wins = 0;
    computer_wins = 0;
    while rounds > 0:
        rounds -= 1

        p_move = playerMove()
        c_move = random.randint(1, 3)
        if p_move == -1:
            print("Invalid move, press any key to repeat round.")
            msvcrt.getch()
            break

        winner = determineWinner(p_move, c_move)
        if winner == "won":
            player_wins += 1
        elif winner == "lost":
            computer_wins += 1

        print("You %s this round." % winner)
        time.sleep(1)
        print("Your Choice: %s" % convert(p_move))
        time.sleep(1)
        print("Computer's Choice: %s" % convert(c_move))
        time.sleep(1.5)
        print("Press any key to continue on to the next round.")
        msvcrt.getch()
        clear()

    print("Overall, the computer won %s times and you won %s times." % (computer_wins, player_wins))


main()
