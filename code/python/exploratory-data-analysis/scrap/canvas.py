import matplotlib.pyplot as plt
import numpy as np

# Simple data to display in various forms
x = ['Darkeness: No street lighting','Darkness: Street lighting unknown',
                    'Darkness: Street lights present and lit', 'Darkness: Street lights present but unlit',
                    'Daylight: Street light present']



ys = [[9226, 1607, 32549, 654, 119518],
 [8132, 1355, 29096, 550, 115281],
 [8002, 1649, 29131, 675, 112017],
 [8505, 3106, 35803, 911, 131390],
 [7295, 2016, 26906, 780, 101663],
 [7199, 1731, 28449, 872, 108071]]



__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"




import matplotlib.pyplot as plt


x = [2009, 2010, 2011, 2012, 2013, 2014]

x = [0, 1, 2, 3, 4]
ys = [[9226, 1607, 32549, 654, 119518],
 [8132, 1355, 29096, 550, 115281],
 [8002, 1649, 29131, 675, 112017],
 [8505, 3106, 35803, 911, 131390],
 [7295, 2016, 26906, 780, 101663],
 [7199, 1731, 28449, 872, 108071]]

ax = plt.subplot(111)
ax.bar(x, ys[0],width=0.2,color='b',align='center')
ax.bar(x, ys[1],width=0.2,color='g',align='center')
ax.bar(x, ys[2],width=0.2,color='r',align='center')

plt.show()

# f, axarr = plt.subplots(3, 2)

# axarr[0, 0].bar(x, ys[0])
# axarr[0, 0].set_title('2009')
# axarr[0, 0].bar(x, ys[1])
# axarr[0, 1].set_title('2010')
# axarr[0, 0].bar(x, ys[2])
# axarr[1, 0].set_title('2011')
# axarr[0, 0].bar(x, ys[3])
# axarr[1, 1].set_title('2012')


plt.show()
