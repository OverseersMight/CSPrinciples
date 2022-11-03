import os
import random


def clear(): os.system("cls")


def toInt(to_convert):
    try:
        return int(to_convert)
    except ValueError:
        return False


def random_list(size):
    lis = []
    possible = []
    for i in range(1, (size) + 1):
        possible.append(i)
    print("Done building list...")
    while size > 0:
        print(size)
        rand = random.randint(0, len(possible)) - 1
        lis.append(possible[rand]*3)
        possible.pop(rand)
        size -= 1
    return lis


print(random_list(100000))
