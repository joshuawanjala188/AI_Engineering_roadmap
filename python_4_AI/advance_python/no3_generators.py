#They provide an easier way to create iterators
"""
instead of manually implementing __iter__()
__next__() you can use yield

yield is different from return 

Consider:

def normal():
    return 10

The function finishes immediately.

A generator:

def generator():
    yield 10
    yield 20
    yield 30

pauses after each yield.

Conceptually:

generator()
    ↓
yield 10
    ↓
pause
    ↓
yield 20
    ↓
pause
    ↓
yield 30
    ↓
finish
"""

def numbers():
    yield 1
    yield 2
    yield 3


for number in numbers():
    print(number)


def generate_number():

    for i in range(100):
        yield i


for number in generate_number():
    print(number)



#List vs Generator

#List
numbers = [x for x in range(100000)]
# it stores all values


#Generator

numbers = (x for x in range(1000000))

"""
List
████████████████████
stores everything

Generator
█
produces → consumes → produces → consumes
"""