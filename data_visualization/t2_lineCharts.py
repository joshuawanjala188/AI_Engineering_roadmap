import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5, 6, 7]
temperature = [24, 25, 26, 25, 27, 28, 26]

plt.plot(days, temperature)

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weekly temperature")

plt.show()