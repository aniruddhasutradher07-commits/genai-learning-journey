import matplotlib.pyplot as plt

marks = [45,67,89,90,55,78,92,60,85,70,95,40,88,76,63]

plt.hist(marks, bins=5)
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.show()