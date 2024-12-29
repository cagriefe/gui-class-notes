# Histogram

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1, size=1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30)

ax.set_title("Histogram")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")

plt.show()