import json

with open('student.json', 'r') as file:
    dt = json.load(file)

name = dt['name']
age = dt['age']
marks = dt['marks']

print(f"name {name}")
print(f"age {age}")
print(f"marks {marks}")
