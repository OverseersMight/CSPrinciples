from time import sleep


def give(put):
    return input("Give a %s: " % put)


def give2(put):
    return input("Give an %s: " % put)


vars = [give("noun"),
        give("noun"),
        give2("adjective"),
        give("noun"),
        give("verb"),
        give("verb"),
        give("verb"),
        give2("adjective"),
        give("task"),
        give("type of candy"),
        give2("adjective"),
        give2("adjective")]

sts = ["On Halloween, you get to go trick-or-treating! Everyone will dress up in costumes, like a/an %s or a/an %s.",
       "This year, you decided to dress up as a/an %s %s.",
       "Your mom takes you and your best friend trick-or-treating.",
       "While you are out, your dad stays at home and %s.",
       "Other fun things to do on Halloween are %s scary movies and %s.",
       "This year, you get lots of %s candy!",
       "When you get home, your dad says he wants some, because he works hard as a %s and he deserves some of your %s.",
       "You are %s but you give it to him anyway.",
       "Dads are so %s but you love him!"]

for x in range(len(sts)):
    cnt = sts[x].count("%s")
    tup = tuple(vars[x:x + cnt])
    print(sts[x] % tup)
    sleep(1)
