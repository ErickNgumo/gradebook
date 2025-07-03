from random import choice

print("Welcome to Gradebook System!")

all_students = []

#Add student and marks
def add_student_details():
    num_students = int(input("How many students do you want to add? \n"))
    for i in range(num_students):
        student_name = input("Enter the student's name: ")
        student_marks = input("Enter the student's marks: ")
        student_details = [student_name,student_marks]
        all_students.append(student_details)
    if num_students == 1:
        print(f'The student {student_name} has been added!')
    else:
        print('The students have been added')


#Display all students and marks
def display_students():
    for student_details in all_students:
        for student in student_details:
            print(student," ", end="")
        print()


#Calculate average mark
def average_marks():
    total_marks = 0
    for student_details in all_students:
        marks = int(student_details[1])
        total_marks += marks
    return total_marks/len(all_students)


#Find top and lowest scorer
def position_score():
    def top_score():
        top_scorer = ""
        top_score = 0
        for student_details in all_students:
            marks = int(student_details[1])
            if marks > top_score:
                top_scorer = student_details[0]
                top_score = marks
        return [top_scorer,top_score]
    def lowest_score():
        lowest_scorer = ""
        lowest_score = 100
        for student_details in all_students:
            marks = int(student_details[1])
            if marks < lowest_score:
                lowest_scorer = student_details[0]
                lowest_score = marks
        return [lowest_scorer,lowest_score]

    return {'top student': top_score(),'lowest student': lowest_score() }


#Search for a student
def search_student():
    search_student = input('Enter Student Name: ')
    student_found = False
    marks = 0
    for student in all_students:
        student_name = student[0]
        if search_student.upper() == student_name.upper():
            student_found = True
            marks = student[1]
            break
    if student_found is True:
        print(f'{search_student} has marks {marks}')
    else:
        print("STUDENT DOESN'T EXIST" )


while True:
    print('''
    Welcome to Gradebook System!

    1. Add student
    2. Show all students
    3. Show average score
    4. Show top and bottom scorers
    5. Search student
    6. Exit
    ''')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        add_student_details()
        break
    elif choice == 2:
        display_students()
    elif choice == 3:
        print(average_marks())
    elif choice == 4:
        print(position_score())
    elif choice == 5:
        search_student()
    elif choice == 6:
        print('Done')
    else:
        print('INVALID ENTRY')





