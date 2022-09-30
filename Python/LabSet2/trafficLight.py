inp = input("What color is the traffic light? \n")
inp = inp.lower()
if inp == "green":
    print("\nCar is allowed to go.")
elif inp == "yellow":
    print("\nCar has to wait")
elif inp == "red":
    print("\nCar has to stop")
else:
    print("Unrecognized input.")
