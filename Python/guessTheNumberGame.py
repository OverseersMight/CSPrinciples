import random
roll = random.randint(1, 100)
guess = None
attempt = 0;
while(guess != roll):
  guess=int(input("Num from 1 - 100: "))
  if guess<roll:
    print("Too low")
  elif guess>roll:
    print("Too high")
print("Spot on")