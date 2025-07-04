import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

# file = open("names.txt")
# print(file.read(5))
# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)
# file.close() # should close the file after opening it

# try:
#     file = open("names.txt")
#     print(file.read())
# except Exception as e:
#     print(f'Error: {e}')
# finally:
#     file.close()

# # Append - adding to files, or creating the file if it doesn't exist
# file = open("names.txt","a")
# file.write("Ngumo\n")
# file.close
#
# file = open("names.txt")
# print(file.read())
# file.close()
#
# # write(overwrite)
# file = open("context.txt", "w")
# file.write("I deleted all of the context")
# file.close()

# file = open("context.txt")
# print(file.read())
# file.close()


#Two ways to create a new file
# creates a file for writing, create a file of it does not exist
#
# f = open("name_list.txt", "w")
# f.write("I fucking did it!")
# f.close()
#
# f = open("name_list.txt")
# print(f.read())
# f.close()
#
# #creates the specified file, but returns an error if the file exists
# if not os.path.exists("numo.txt"):
#     f = open("numo.txt", "x")
#     f.close()

# Delete a file
# Avoid an error if it doesn't exist
# if os.path.exists("numo.txt"):
#     os.remove("numo.txt")
# else:
#     print('The file does not exist')
#
# with open("more_names.txt") as f:
#     content = f.read()
# with open("names.txt", "w") as f:
#     f.write(content)

details = [['Jane', 90],['Alex', 91],['Hiram', 88]]
file = open("names.txt","w")
for students_details in details:
    for students_marks in students_details:
        name = students_details[0]
        marks = students_details[1]
    file.write(f"{name} - {marks}\n")
file.close()

file = open("names.txt")
print(file.read())

