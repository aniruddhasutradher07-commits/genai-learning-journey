import matplotlib.pyplot as plt

subjects = ["Biochem","Bioinformatics","Optics","Python"]
marks = [85,92,78,95]

plt.bar(subjects,marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject-wise Marks")
plt.show()