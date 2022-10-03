def first():
    print("Inside first function")


def second():
    print("Inside second function")
    first()


def third():
    print("Inside third function")
    first()
    second()


def main():
    first()
    third()
    second()
    third()


main()
