row1 = ["🎁" , "🎁" , "🎁"]
row2 = ["🎁" , "🎁" , "🎁"]
row3 = ["🎁" , "🎁" , "🎁"]

map = [row1, row2 , row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")
h = int(position[0]) #2
v = int(position[1]) #3
s_po = map[v-1]
s_po[h - 1] = "x"

print(f"{row1}\n{row2}\n{row3}")