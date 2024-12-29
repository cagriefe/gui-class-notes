# Pie Chart

import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 30, 20, 10]
explode = [0.1, 0, 0, 0]

fig, ax = plt.subplots()

ax.pie(sizes, labels=labels, explode=explode, autopct="%.1f%%", shadow=True, startangle=90)
ax.set_title("Pie Chart")

plt.show()