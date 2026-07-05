import random 
letters = ['q','w','e','r','t','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
number = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','#','%','+','*','$','&','()',')']
print("Wellcome to PyPassword Generator!")
nr_letters = int(input("How many letters do you want in your password?\n"))
nr_number = int(input("How many number would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_list = []
for char in range(1 , nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1 , nr_number + 1):
    password_list += random.choice(number)
for char in range(1 , nr_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is: {password}")
