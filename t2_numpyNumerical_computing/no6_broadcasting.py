import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(x+ 10)


#Reshaping

x2 = np.arange(12)
print(x2)

x2 = x2.reshape(3, 4)
print(x2)


#Flattening - convert a multidimensional array into one dimension

x = np.array([
    [1, 2],
    [3, 4]
])

flat = x.flatten()
print(flat)

#Transpose
x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(x.T)

#Matrix multiplication

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

c = A @ B
print("Multiplication:", c)

#Dot product 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)

print("Dot product:",result)


#random numbers

rng = np.random.default_rng()

weights = rng.random((3, 4))
print(weights)

rng = np.random.default_rng(42)

print(rng.random(5))