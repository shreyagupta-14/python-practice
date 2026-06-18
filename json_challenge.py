import json

student_details = [
    {"name":"Shreya", "age": 21, "passed_exam":True},
    {"name":"Rahul", "age": 25, "passed_exam":False},
    {"name":"Tina", "age": 18, "passed_exam":True}
]

with open("student.json","w") as file:
    json.dump(student_details,file, indent=4)

with open("student.json", "r") as file:
    loaded_data = json.load(file)

for student in loaded_data:
    if student['passed_exam']:
        status = "passed"
    else:
        status = "failed"
        
    print(f"Student {student['name']} is {student['age']} years old and has {status} the exam.")