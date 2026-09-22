import matplotlib.pyplot as plt

countries = ["Kenya", "Uganda", "Tanzania"]
students = [50, 35, 42]

plt.barh(countries, students) # vertical
#plt.barh(countries, students) # horizontal bar graph

plt.xlabel("Country")
plt.ylabel("Students")

plt.title("Students by country")

plt.show()