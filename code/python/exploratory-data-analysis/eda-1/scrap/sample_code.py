import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

items = ['Darkeness: No street lighting','Darkness: Street lighting unknown',
             'Darkness: Street lights present and lit', 
             'Darkness: Street lights present but unlit',
             'Daylight: Street light present']

years = list(range(2009, 2015, 1))


ys = [[9226, 1607, 32549, 654, 119518],
 [8132, 1355, 29096, 550, 115281],
 [8002, 1649, 29131, 675, 112017],
 [8505, 3106, 35803, 911, 131390],
 [7295, 2016, 26906, 780, 101663],
 [7199, 1731, 28449, 872, 108071]]

ys = [[row[j] for row in ys] for j in range(5)]
pos = list(range(len(years))) 

width = 0.15

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,6))


plt.bar(pos, 
        ys[0], 
        width, 
        alpha=0.5, 
        color='#9b2f29', 
        label=items[0]) 


plt.bar([p + width for p in pos], 
        ys[1],
        width, 
        alpha=0.5, 
        color='#EE3224', 
        label=items[1]) 


plt.bar([p + width*2 for p in pos], 
        ys[2], 
        width, 
        alpha=0.5, 
        color='#F78F1E', 
        label=items[2]) 


plt.bar([p + width*3 for p in pos], 
        ys[3], 
        width, 
        alpha=0.5, 
        color='#FFC222', 
        label=items[3]) 

plt.bar([p + width*4 for p in pos], 
        ys[4], 
        width, 
        alpha=0.5, 
        color='#000000', 
        label=items[4]) 


# Set the y axis label
ax.set_ylabel('Accident Count')

# Set the chart's title
ax.set_title('Accidents by lightning conditions over the years')

# Set the position of the x ticks
ax.set_xticks([p + 1 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(years)

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*8)
plt.ylim([0, max(ys[0] +  ys[1] + ys[2] + ys[3] + ys[4]) + 40000])

# Adding the legend and showing the plot
plt.legend(items, loc='upper left')
plt.grid()
plt.show()
