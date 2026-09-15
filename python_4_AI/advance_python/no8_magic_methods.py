"""
27. Magic Methods

Magic methods, or dunder methods, allow Python objects to interact with built-in Python operations.

Examples:

__init__
__str__
__repr__
__len__
__eq__
__add__
__getitem__
__iter__
__next__
28. __str__
class Model:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Model: {self.name}"

Now:

model = Model("Classifier")

print(model)

Output:

Model: Classifier
29. __len__
class Dataset:

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

Now:

dataset = Dataset([1, 2, 3, 4])

print(len(dataset))

Output:

4

This is particularly relevant to ML datasets.

30. __getitem__

This allows an object to support indexing.

class Dataset:

    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

Now:

dataset = Dataset(["A", "B", "C"])

print(dataset[0])

Output:

A

This kind of interface is commonly used by dataset abstractions.

31. __iter__

You can make an object iterable.

class Dataset:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

Then:

dataset = Dataset([1, 2, 3])

for item in dataset:
    print(item)

"""