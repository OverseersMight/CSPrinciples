import os
import random


def clear(): os.system("cls")


def toInt(to_convert):
    try:
        return int(to_convert)
    except ValueError:
        return False


def randlist(size):
    lis = []
    while size > 0:
        lis.append(random.randint(0, 10))
        size = size - 1
        if size % 100000 == 0:
            print("Current size is %s" % len(lis))
    return lis
