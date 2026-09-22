import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]

model_a = [0.9, 0.7, 0.5, 0.4, 0.3]
model_b = [0.9, 0.8, 0.7, 0.6, 0.5]

plt.plot(months, model_a, label="Model A")
plt.plot(months, model_b, label="Model B")

plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.title("Model Training")

plt.legend()
plt.savefig("scores.png") # saving a graph

plt.show()


"""
18. Figure and Axes

As you progress into AI engineering, you'll often see:

fig, ax = plt.subplots()

Think of it like:

Figure
└── Axes
     └── actual graph

Example:

fig, ax = plt.subplots()

ax.plot(hours, scores)

ax.set_xlabel("Hours")
ax.set_ylabel("Score")
ax.set_title("Study Hours vs Score")

plt.show()

This approach gives you more control and becomes especially useful for larger visualization projects.

19. Subplots

You can create multiple graphs in one figure.

fig, axes = plt.subplots(1, 2)

axes[0].plot(hours, scores)
axes[0].set_title("Line Plot")

axes[1].scatter(hours, scores)
axes[1].set_title("Scatter Plot")

plt.show()
"""