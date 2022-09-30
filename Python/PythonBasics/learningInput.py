put=input("What is your age?\n")
if put.isdigit():
  print("Your age is %s in 30 years." % (int(put)+30))
else:
  print("Invalid number: %s" % (put))