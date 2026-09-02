#this is shoreteningg the lists

numbers = [i for i in range(10)]

print(numbers)

#square numbers

squares = [x**2 for x in range(1, 10)]
print(squares)



even_numbers = [
    x for x in numbers
    if x% 2 == 0
]

print(even_numbers)