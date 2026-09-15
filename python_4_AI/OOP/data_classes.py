#Python provides dataclass for classes primarily used to store data

from dataclasses import dataclass

@dataclass

class Student:
    name: str
    score: float

student = Student("Alice", 85)
print(student)