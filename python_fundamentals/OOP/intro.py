#oop is a way of organizing programs around objects
"""An object combines:

Data → attributes
Behavior → methods

For example, an AI model could have:

Model
├── name
├── learning_rate
├── weights
├── train()
├── predict()
└── evaluate()

Instead of keeping all these things separate, we can put them into a class.

Classes - a class is like a blueprint

class Student:
    pass


    we havent created a class first that's only a blueprint


Objects- an objects is a instance of a class

class Student:
    pass

student1 = Student()
student2 = Student()

Now we have two different objects:

Student class
      │
      ├── student1
      │
      └── student2

Both were created from the same blueprint.

Attributes- store more information about an object

class Student:
    pass


student = Student()

student.name = "Alice"
student.score = 85

"""

#The _init_() method it is used to assign attributes

class Student:

    def __init__(self, name, score):

        self.name = name  #self refer to the current object self.name = name means store the supplied name inside this particular object
        self.score = score
#Now create an object
#methods - they are functions that belong to a class

    def introduce(self):

        print(f"My name is {self.name}")

    def passed(self):
        if self.score >= 40:
            return f"{self.name} has passed"   

        else:
            return "Failed"

student = Student("Joshua", 40)
student.introduce()
print(student.passed())

"""11. Instance Attributes

These belong to individual objects.

class Model:

    def __init__(self, name, learning_rate):
        self.name = name
        self.learning_rate = learning_rate

Create:

model1 = Model("Model A", 0.001)
model2 = Model("Model B", 0.01)

They have different values:

model1
├── name = Model A
└── learning_rate = 0.001

model2
├── name = Model B
└── learning_rate = 0.01

Class Attributes

A class attribute belongs to the class rather than a particular instance.

class Model:

    framework = "PyTorch"

    def __init__(self, name):
        self.name = name

Now:

model = Model("Classifier")

print(model.name)
print(model.framework)

Output:

Classifier
PyTorch

framework is shared by instances unless overridden.

Class Attributes- belongs to the class rather than a particular instance

class Model:

    framework = "Pytorch"

    def __init__(self, name):

        self.name = name


model = Model("Classifier")
print(model.name, model.framework)
Instance vs Class Attributes

Think:

Class
│
├── framework = "PyTorch"    ← class attribute
│
├── model1
│    └── name = "CNN"        ← instance attribute
│
└── model2
     └── name = "Transformer" ← instance attribute

Use instance attributes for data that varies between objects.

Use class attributes for information shared across instances.

Instance
        
"""




