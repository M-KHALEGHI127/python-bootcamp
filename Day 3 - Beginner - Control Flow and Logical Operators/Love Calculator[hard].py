print("welcome to  Love Calculator!!!")
name1 = input("what is your name?\n")
name2 = input("what is their name?\n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
name = f"{lower_name1} {lower_name2}"
count_namet = name.count("t")
count_namer = name.count("r")
count_nameu = name.count("u")
count_namee = name.count("e")
count_namel = name.count("l")
count_nameo = name.count("o")
count_namev = name.count("v")
count_namee = name.count("e")
num1 = count_namet + count_namer + count_nameu + count_namee
num2 = count_namel + count_nameo + count_namev + count_namee
score = f"{num1}{num2}"
score2 = int(score)
if score2 < 10 or score2 > 90:
    print(f"your score is {score2}, you go together like coke and mentos")
elif 40 <= score2 <=50:
    print(f"your score is {score2}, you are good ")
else:
    print(f"your score is {score2}")
    