import random

chose = int(input("what do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if chose == 0 :
    print("You chose: Rock")
if chose == 1 :
    print("You chose: Paper")
if chose == 2 :
    print("You chose: Scissores")

cump_chose = random.randint(0 , 2)

if cump_chose == 0 :
    print("cumputer chose: Rock")
if cump_chose == 1 :
    print("cumputer chose: Paper")
if cump_chose == 2 :
    print("cumputer chose: Scissores")

if chose == 0 and cump_chose == 1 :
    print("you lose!")
if chose == 1 and cump_chose == 2 :
    print("you lose!")
if  chose == 2 and cump_chose ==0 :
    print("you lose!")


if chose == 0 and cump_chose == 2:
    print("you win!!!!")
if chose == 1 and cump_chose == 2:
    print("you win!!!!")
if chose == 2  and cump_chose == 1 :
    print("you win!!!!")

if cump_chose == chose :
    print("it's draw!!!")