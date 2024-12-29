# Scatter plot

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values)

ax.set_title("Scatter Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

plt.show()