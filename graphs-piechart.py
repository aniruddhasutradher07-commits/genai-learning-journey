import matplotlib.pyplot as plt

subjects = ["Biochem","Bioinformatics","Optics","Python"]
marks = [85,92,78,95]

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()