

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"



import numpy as np
import matplotlib.pyplot as plt

# data = [[5., 25., 50., 20.],
#   [4., 23., 51., 17.],
#   [6., 22., 52., 19.]]


ys = [[9226, 1607, 32549, 654, 119518],
 [8132, 1355, 29096, 550, 115281],
 [8002, 1649, 29131, 675, 112017],
 [8505, 3106, 35803, 911, 131390],
 [7295, 2016, 26906, 780, 101663],
 [7199, 1731, 28449, 872, 108071]]

#ys = [[row[j] for row in ys] for j in range(5)]


#X = list(range(2009, 2015))
X = np.arange(5)

plt.bar(X + 0.00, ys[0], color = 'b', width = 0.25)
plt.bar(X + 0.25, ys[1], color = 'g', width = 0.25)
plt.bar(X + 0.50, ys[2], color = 'r', width = 0.25)
plt.bar(X + .75, ys[3], color = 'y', width = 0.25)
plt.bar(X + 1.00, ys[4], color = 'g', width = 0.25)

plt.show()
