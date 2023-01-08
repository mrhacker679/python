student = []

with open('short.txt') as file:
    for line in file:
        new = line.split()
        student.append(new[1])
student.remove('student')
print(student)
print(f"The total no of students in the class is {len(student)}")

marks = []
with open('attachment.txt') as f:
    for line in f:
        if line.startswith('Geography'):
            stu = line.split()
            marks.append(stu[2])
            marks.sort()

print(f"The third lowest marks of the Geography is {marks[2]}")
