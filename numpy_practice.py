import numpy as np

arr = np.arange(1,21)
print("Array:", arr)

even = arr[arr % 2 == 0]
print("Even numbers:", even)

print("Sum:", arr.sum())
print("Mean:", arr.mean())

matrix = arr.reshape(4,5)
print("Matrix:\n", matrix)