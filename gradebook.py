import csv

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

    with open("student_details.csv","a",newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(all_students)

    if num_students == 1:
        print(f'The student {student_name} has been added!')
    else:
        print('The students have been added')
    all_students.clear()


#Display all students and marks
def display_students():
    with open("student_details.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'{row[0]} - {row[1]}')

#Calculate average mark
def average_marks():
    total_marks = 0
    student_count = 0
    with open("student_details.csv","r") as file:
        reader = csv.reader(file)
        for rows in reader:
            marks = float(rows[1])
            total_marks += marks
            student_count += 1
    if student_count == 0:
        return 0
    return total_marks/student_count

#Find top and lowest scorer
def position_score():
    def top_score():
        top_scorer = ""
        top_score = 0
        with open("student_details.csv", "r") as file:
            reader = csv.reader(file)
            for rows in reader:
                if len(rows[1]) < 2 or not rows[1].isdigit():
                    continue
                marks = float(rows[1])
                if marks > top_score:
                    top_scorer = rows[0]
                    top_score = marks
        return [top_scorer,top_score]
    def lowest_score():
        lowest_scorer = ""
        lowest_score = 100
        with open("student_details.csv", "r") as file:
            reader = csv.reader(file)
            for rows in reader:
                if len(rows[1]) < 2 or not rows[1].isdigit():
                    continue
                marks = float(rows[1])
                if marks < lowest_score:
                    lowest_scorer = rows[0]
                    lowest_score = marks
        return [lowest_scorer, lowest_score]

    return  {
        'top student': top_score(),
        'lowest student': lowest_score()
    }



#Search for a student
def search_student():
    search_student = input('Enter Student Name: ')
    student_found = False
    marks = 0
    with open("student_details.csv", "r") as file:
        reader = csv.reader(file)
        for rows in reader:
            student_name = rows[0]
            if search_student.upper() == student_name.upper():
                student_found = True
                marks = rows[1]
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
        result = (position_score())
        top_student = result['top student']
        low_student = result['lowest student']
        print(f'The Top Student is {top_student[0]}, with a score of {top_student[1]}')
        print(f'The Lowest Student is {low_student[0]}, with a score of {low_student[1]}')
    elif choice == 5:
        search_student()
    elif choice == 6:
        print('Done')
        break
    else:
        print('INVALID ENTRY')





