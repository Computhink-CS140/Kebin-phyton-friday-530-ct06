print("Hello from lesson 6")
sum = 0

total_num_students = int(input("what is the total number of students?"))
for i in range (total_num_students):
    marks = int(input("what is the marks for this student: "))
    sum += marks
print(sum)
average = sum/total_num_students
print("class avg = " + str(average))