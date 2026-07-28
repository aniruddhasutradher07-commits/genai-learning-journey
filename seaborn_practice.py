import seaborn as sns 
import matplotlib.pyplot as plt

subjects = ["Biochem","Bioinformatics","Optics","Python"]
marks = [85,92,78,95]

sns.barplot(x=subjects, y=marks)
plt.title("Subject-wise Marks (Seaborn)")
plt.show()