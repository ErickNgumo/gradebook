# import json
# employee = {
#     "name": "Erick",
#     "age": 30,
#     "job": "cook"
# }
# file_path = "output.json"
# with open(file_path, "w") as f:
#     json.dump(employee, f, indent = 2)
#     print("JSON file was created")
#
# with open(file_path, "r") as f:
#     print(f.read())

import csv
employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy ", 27, "Scientist"]
]

with open("output.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    print(f'output.csv was created')
    for row in employees:
        writer.writerow(row)
# with open("output.csv") as f:
#     print(open(f.read()))