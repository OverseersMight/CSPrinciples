import os
import random


def clear(): os.system("cls")


def toInt(to_convert):
    try:
        return int(to_convert)
    except ValueError:
        return False


def create_choices(nums):
    clear()
    inp = input("Please type the number you want added to the list, termination condition is 'done'\n")
    if inp == "done":
        return nums
    if not inp:
        return create_choices(nums)
    nums.append(inp)
    return create_choices(nums)


def random_choice(nums):
    return nums[random.randint(0, len(nums)-1)]
