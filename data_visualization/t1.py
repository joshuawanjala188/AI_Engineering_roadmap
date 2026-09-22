import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
scores = [45, 50, 60, 70, 85]


plt.plot(hours, scores)
plt.xlabel("Hours studied")
plt.ylabel("Exam score")
plt.title("Study hours vs Exam Score")
plt.grid()

plt.show()