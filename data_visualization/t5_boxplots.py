
"""
A box plot is useful for understanding:

median
spread
quartiles
possible outliers


import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 61, 65, 68, 70, 72, 75, 80, 85, 90]

plt.boxplot(scores)
plt.ylabel("Score")
plt.title("Score distribution")

plt.show()"""
import matplotlib.pyplot as plt

kenya = [70, 75, 80, 85, 90]
uganda = [50, 55, 60, 65, 70]
tanzania = [60, 65, 70, 75, 80]

plt.boxplot([kenya, uganda, tanzania])

plt.xticks(
    [1, 2, 3],
    ["Kenya", "Uganda", "Tanzania"]
)

plt.ylabel("Score")
plt.title("Scores by Country")

plt.show()