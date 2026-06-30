height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

MBI = weight / (height ** 2)
rmbi = round(MBI , 2)
if rmbi > 18.5 : 
    print(f"your mbi is: {rmbi}, you are underweight!!")
elif 18.5 <= rmbi < 25:
    print(f"your mbi is: {rmbi}, you are normal weight!!")
elif 25 <= rmbi < 30 :
    print(f"your mbi is: {rmbi}, you are overweight!!")
elif 30 <= rmbi < 35 :
    print(f"your mbi is: {rmbi}, you are obese!!")
elif 35 <= rmbi:
    print(f"your mbi is: {rmbi}, you are clinically obese!!")