eng = int(input("What grade do you have in English? "))
math = int(input("What grade do you have in Math? "))
sci = int(input("What grade do you have in Science? "))
hist = int(input("What grade do you have in History? "))
elec = int(input("What grade do you have in your elective? "))

avg = (eng+math+sci+hist+elec)/5

if avg < 45:
    print("Fail")
elif avg < 60:
    print("pass")
elif avg < 75:
    print("good")
elif avg < 85:
    print("very good")
elif avg < 100:
    print("excellent")
else:
    print("Invalid result")
