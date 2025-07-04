marks = int(input('Enter you marks: '))
if marks > 100 or marks < 0:
    print('Invalid Marks!, Please enter valid marks')
elif marks >=70:
    print('Grade A')
elif marks >=60:
    print('Grade B')
elif marks >= 50:
    print('Grade C')
elif marks >= 40:
    print('Grade D')
else:
    print('Grade E')