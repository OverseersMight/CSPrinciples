import random

des = int(input("What is your desired number? "))

rand = random.randint(1, 6)
rand2 = random.randint(1, 6)

while rand + rand2 != des:
    print("%s and %s" % (rand, rand2))
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
print("%s and %s" % (rand, rand2))
