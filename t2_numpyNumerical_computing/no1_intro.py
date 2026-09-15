"""
numpy gives you efficient mathematical computation
1. What is NumPy?

NumPy = Numerical Python

Install it:

pip install numpy

Import it:

import numpy as np

The main object in NumPy is the array.

import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)

Output:

[10 20 30 40]
2. Why NumPy?

Python lists work:

numbers = [1, 2, 3, 4]

But AI systems often work with thousands, millions, or billions of numbers.

NumPy provides:

fast numerical operations
multidimensional arrays
vectorized calculations
matrix operations
linear algebra
random-number generation
statistical operations
efficient memory usage

For example:

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)

Output:

[11 22 33 44]

Instead of manually looping through every element.
"""

import numpy as np

x = np.array(
    [ 
    [1, 2, 3],
    [4, 5, 6]
    ]
)


#Dimensions - it tell us how many dimensions an array has

print(x.ndim)

#Shape tell you the size of every dimension

print(x.shape)#(2, 3) menaning 2 rows 3 columns

#Size tell us the total number of elements

print(x.size) # 6

#Data type - numpy have a datatype
print(x.dtype)

# You can specify the type

x2 = np.array([1, 2, 3], dtype=np.float32) # this matters greatyly because the models often use different types to reduce memory usage and speed up computation


print(x2.dtype)


#Special Arrays

x = np.zeros((3, 4))
print(x)

#full()

x = np.full((2, 3), 7)

print(x)

#arrage - similar to python range()

x = np.arange(0, 10)
print(x)

#linspace()  creates evenly spaced numbers, useful for mathematical functions, graphs, simulations, numerical analysis


x = np.linspace(0, 2, 5)
print(x)


#Indexing numpy indexing starts at zero
x = np.array([1, 2, 3, 4, 5])
print(x[0])


#2D indexing

x = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(x[0, 1])

#Slicing
x = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(x[:, :2]) #x[rows, columns]

#Changing values

x = np.array([1, 2, 3])
x[1] = 99
print(x)



