import random

test_seed = int(input("create a seed number:"))
random.seed(test_seed)
#for testing program
print("tossing a coin!!")
rand = random.randint(1,2)
if rand == 1 :
    print("Heads")

if rand == 2 :
    print("Tails")
