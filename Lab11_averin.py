grades = []
students_passed = []
valid_input = True

while True:
    grade = input("Enter Grade (type 'done' to stop): ")

    if grade.lower() == 'done':
        break
    if not grade.isdigit():
        print("Error, this is not a numerical value.")
    else:
        grade = int(grade)
        if grade <= 40 or grade > 100:
            print("Invalid, please try again.")
            valid_input = False
            break
        else:
            grades.append(grade)
            if grade >= 75:
                students_passed.append(grades)

if valid_input:
    if grades:
        average = sum(grades) / len(grades)
        passing_percent = (len(students_passed) / len(grades)) * 100
        print(f"Grades: {grades}")
        print(f"Average: {average:.2f}")
        print(f"Passing Percentage: {passing_percent:.2f}%")
        print(f"Student Passed: {len(students_passed):.2f}")
    else:
        print("No Grades input.")