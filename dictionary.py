student = {
    "naam": "Aniruddha",
    "age": 20,
    "college": "Centurion University of Technology and Managment",
    "favourite_subject": "Python"
}

print(student["naam"])
print(student["age"])
print(student["college"])
print(student["favourite_subject"])

student["age"] = 21
student["favourite_subject"] = "MLUP"


for key, value in student.items():
    print(key, ":", value)