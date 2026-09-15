#It happens when an inner function remembers variables from its surrounding function

def create_multiplier(multiplier):

    def multiply(number):

        return number * multiplier

    return multiply

double = create_multiplier(2)
print(double(5))