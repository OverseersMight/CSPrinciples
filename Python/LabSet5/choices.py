import os
import random


def clear(): os.system("cls")


def toInt(to_convert):
    try:
        return int(to_convert)
    except ValueError:
        return False


def create_choices(numlist):
    clear()
    inp = input("Please type the number you want added to the list, termination condition is 'done'\n")
    if inp == "done":
        return numlist
    if not inp:
        return create_choices(numlist)
    numlist.append(inp)
    return create_choices(numlist)


def main():
    choices = create_choices([])
    print(choices[random.randint(0, len(choices)-1)])


main()
