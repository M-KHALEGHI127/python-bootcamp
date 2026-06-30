student_scored = input("Input a list of student: ").split()
for n in range(0, len(student_scored)):
    student_scored[n] = int(student_scored[n])
print(student_scored)

high_score = 0
for score in student_scored:
    if score > high_score:
        high_score = score

print(f"the high score is: {high_score}")