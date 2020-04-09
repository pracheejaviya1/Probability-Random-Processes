# This program allows the user to hover on the plot. x,y co-ordinates are printed in the terminal. Storing these
# values in the repective list and plotting the same gives us the desired plot.

import matplotlib.pyplot as plt


def mouse_move(event):
    x, y = event.xdata, event.ydata
    print(x, y)


plt.connect('motion_notify_event', mouse_move)
plt.plot(1, 1)
plt.grid()
plt.xlim(2, 10)
plt.ylim(0.001, 10000)
plt.yscale("log")
plt.xlabel('Magnitude in Ritcher Scale')
plt.ylabel('Number of earthquakes with M>m')
plt.show()
