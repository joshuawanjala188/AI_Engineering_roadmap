#A decorator allows you to modify or extend a function behavior without changing the function itself




#But decorators make this reusable


""" 

def my_decorator(function):

    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper  

@my_decorator
def greet():

    print("Hello")


greet()"""

#Decorators with arguments

def my_decorator(function):

    def wrapper(*args, **kwargs):

        print("Before")

        result = function(*args, **kwargs)

        print("After")

        return result

    return wrapper


@my_decorator
def add(a, b):

    return a + b

result = add(10, 20)
print("Add: ",result)



