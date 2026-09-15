#Takes another function as an argument
#Return another function


def apply_operation(a, b, operation):

    return operation(a, b)


def add(a, b):

    return a + b

def multiply(a, b):

    return a * b


print(apply_operation(4, 2, multiply))
print(apply_operation(2, 2, add))