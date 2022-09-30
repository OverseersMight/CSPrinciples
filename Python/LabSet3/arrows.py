def seg1():
    return " /\\\n" \
           "/  \\\n"


def seg2():
    return " ||\n" " ||\n"


def seg3():
    return "\\  /\n" \
           " \\/\n"


print("%s\n%s\n%s%s\n%s%s" % (seg1(), seg1(), seg2(), seg1(), seg3(), seg1()))
