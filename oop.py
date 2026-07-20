class Student:
    def __init__(self, naam, age):
        self.naam = naam
        self.age = age
        
    def introduce(self):
        print("Mera naam", self.naam, "hai aur main", self.age,"saal ka hoon")
    
    def add_marks(self,marks):
        self.marks = marks
        print(self.naam, "ke marks hain:", self.marks)

student1 = Student("Amiruddha", 20)
student2 = Student("Disha",20)

student1.introduce()
student2.introduce()
student1.add_marks(85)
student2.add_marks(90)

print(student1.naam)
print(student1.age)
print(student1.marks)

print(student2.naam)
print(student2.age)
print(student2.marks)