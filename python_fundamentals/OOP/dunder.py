"""28. Dunder Methods

Python has special methods surrounded by double underscores.

They're often called dunder methods.

Examples:

__init__
__str__
__repr__
__len__
__eq__
29. __str__

Controls the human-readable representation of an object.

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"

Now:

student = Student("Alice", 85)

print(student)

Output:

Alice: 85
30. __len__

You can define what len() means for your object.

class Dataset:

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

Now:

dataset = Dataset([1, 2, 3, 4, 5])

print(len(dataset))

Output:

5

This is particularly relevant to ML datasets.
"""
