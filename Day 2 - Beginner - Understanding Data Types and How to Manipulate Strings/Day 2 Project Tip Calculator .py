print("Welcome to tip calculator!!!!!")
total_bill = float(input("what was the total bill?\n"))
tip= int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
tip2 = (tip / 100) + 1
bill_tip = tip2 * total_bill
people = int(input("How many people to split the bill?\n"))
total = bill_tip / people 

print(f"Each person should pay: {round(total, 2)}")
               