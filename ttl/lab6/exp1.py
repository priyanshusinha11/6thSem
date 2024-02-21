import numpy as np
from scipy.stats import mode as md

# NumPy arrays using different methods
a = np.array([1, 2, 3, 4, 5])
z = np.zeros((2, 3)) 
o = np.ones((3, 2))  
r = np.arange(10) 

#mathematical operations 
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

add = x + y
sub = x - y
mul = x * y
div = y / x

# indexing and slicing 
s = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
slc = s[0:2, 1:3]

#  statistical analysis
stats = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean = np.mean(stats)
median = np.median(stats)
mode_result = md(stats)[0]  

# reshaping and transposing NumPy arrays
rs = np.arange(12).reshape(3, 4) 
t = np.transpose(rs)  

print("Array from list:", a)
print("Array of zeros:\n", z)
print("Array of ones:\n", o)
print("Array using arange:", r)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Sliced array:\n", slc)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode_result)
print("Reshaped array:\n", rs)
print("Transposed array:\n", t)
