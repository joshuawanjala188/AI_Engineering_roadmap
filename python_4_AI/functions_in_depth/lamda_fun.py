#It is a small anonymous function

"""square = lambda x: x**2

number = int(input("Enter a number: "))
print(square(number))"""

students = [
    {"name": "Alice", "score": 80},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 70}
]

students.sort(
    key= lambda student: student["score"]
)

print(students)
