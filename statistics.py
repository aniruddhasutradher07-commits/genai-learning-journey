import numpy as np
marks = [89,90,80,92,80]

mean = sum(marks)/ len(marks)
print("Mean:", mean)

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))