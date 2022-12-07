def top():
    return "  _______\n /       \\\n/         \\"


def bottom():
    return "\\         /\n \\_______/"


def special():
    return "-\"-'-\"-'-\"-"


def egg():
    return "%s\n%s" % (top(), bottom())


print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (egg(), special(), egg(), special(), bottom(), top(), special(), bottom()))
