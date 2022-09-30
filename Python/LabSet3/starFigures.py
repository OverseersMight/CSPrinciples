def seg1():
    return ("*****\n"
            "*****\n"
            " * *\n"
            "  *\n"
            " * *\n")


def seg2():
    return ("*****\n"
            "*****\n"
            "\n"
            "  *\n"
            "  *\n"
            "  *\n")


print(seg1() + "\n" + seg1() + seg2() + seg1())
