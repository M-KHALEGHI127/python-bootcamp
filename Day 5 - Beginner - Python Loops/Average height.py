student_heights = input("Input a list of student height ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#print(student_heights)
sum = 0
for x in range(0, len(student_heights)):
    
    sum +=   student_heights[n]
#print( sum)
num = 0
for h in student_heights:
    num += 1

#print(num)
ave = sum / num

print(ave)
