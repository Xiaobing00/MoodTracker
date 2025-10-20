# This file tests plotting mood graph.

import matplotlib.pyplot as plt

x = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
y = [5, 6, 7, 8, 9, 6, 4]

plt.plot(x, y, marker='o')
plt.ylim(0, 10)
plt.title("Mood Experiment Graph")
plt.xlabel("Day")
plt.ylabel("Mood")
plt.grid(True)
plt.show()