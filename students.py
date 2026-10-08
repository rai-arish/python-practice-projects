n = int(input('Enter number of students:'))

students = {}
for i in range(n):
    name = input('Enter student name:')
    age = int(input('Enter student age:'))
    student_class = int(input('Enter student class:'))
    roll_no = int(input('Enter student roll number:'))
    marks = float(input('Enter student marks:'))

    student = {
            'name': name,
            'age': age,
            'class': student_class,
            'roll_no': roll_no,
            'marks': marks
     }
    students[roll_no] = student
print(students)