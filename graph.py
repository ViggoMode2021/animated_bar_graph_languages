from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers, PillowWriter
import numpy as np

fig = plt.figure(figsize = (7,5))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 300)
palette = ['red', 'blue', 'green', 'darkorange', 'purple', 'black']

y1, y2, y3, y4, y5, y6 = [], [], [], [], [], []

def animation_function(i):
    y1 = i
    y2 = 5 * i
    y3 = 3 * i
    y4 = 2 * i
    y5 = 6 * i
    y6 = 3 * i

    plt.xlabel("Language")
    plt.ylabel("Speakers")

    plt.bar(["Arabic/French(tie)", "Spanish", "Chinese",
             "Vietnamese", "English", "Tagalog"],
    [y1, y2, y3, y4, y5, y6],
    color = palette)

plt.title("Most spoken languages in the USA (Wikipedia.org)")

animation = FuncAnimation(fig, animation_function, interval = 50)
#Below is the save as gif functionality.

anim = FuncAnimation(fig, animation_function, frames=60, interval=50)
anim.save('languages.gif', writer=PillowWriter(fps=20))

plt.show()
