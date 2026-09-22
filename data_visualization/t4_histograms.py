"""A histogram shows the distribution of numerical data
Histograms are useful for understanding:

distribution
spread
skewness
possible outliers
concentration of values
"""
import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 61, 65, 68, 70, 72, 75, 80, 85, 90]

plt.hist(scores, bins=20)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Distribution of scores")
plt.show()