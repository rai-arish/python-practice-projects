students = {}

while True:
    try:
        n = int(input("Enter number of students: ").strip())

        if n < 0:
            print("Number cannot be negative!")

        elif n > 100:
            print("Too many students! Maximum limit is 100.")

        else:
            break

    except ValueError:
        print("Please enter a valid whole number!")

for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    name = input("Enter name: ").strip()

    while True:
        try:
            age = int(input("Enter age: ").strip())

            if age < 0:
                print("Age cannot be negative!")
            elif age > 100:
                print("Please enter a valid age!")
            else:
                break

        except ValueError:
            print("Age must be a whole number!")

    student_class = input("Enter class: ").strip()

    while True:
        try:
            roll_no = int(input("Enter roll number: ").strip())

            if roll_no <= 0:
                print("Roll number must be positive!")

            elif roll_no in students:
                print("This roll number already exists!")

            else:
                break

        except ValueError:
            print("Please enter a valid whole number!")

    while True:
        try:
            marks = float(input("Enter marks (0-100): ").strip())

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100!")
            else:
                break

        except ValueError:
            print("Please enter valid numeric marks!")

    students[roll_no] = {
        "name": name,
        "age": age,
        "class": student_class,
        "marks": marks
    }

print("\nStudent Records:")
print(students)