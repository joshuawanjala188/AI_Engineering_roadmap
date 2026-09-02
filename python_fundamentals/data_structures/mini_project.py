
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 45},
    {"name": "Charlie", "score": 72},
    {"name": "David", "score": 91}
]

print("ALL STUDENTS")

for student in students:
    print(student["name"])

print("STUDENTS WHO PASSED")

for student in students:
    if student["score"] >= 50:
        print(f"{student['name']}: {student['score']}")


print("AVERAGE SCORE: ")

total_score = sum(student['score'] for student in students)
average_score = total_score / len(students)

print("Average Score:", average_score)

print("\n Highest score")

highest_score = max(student['score'] for student in students)
print(highest_score)

high_scorers = [
    student for student in students
    if student["score"] >= 70
]

print("\nStudents who scored 70 or higher:")
for student in high_scorers:
    print(student["name"], "-", student["score"])