import matplotlib.pyplot as plt

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


years = list(range(2009, 2015, 1))
width = 0.25 

ys = [[9226, 1607, 32549, 654, 119518],
 [8132, 1355, 29096, 550, 115281],
 [8002, 1649, 29131, 675, 112017],
 [8505, 3106, 35803, 911, 131390],
 [7295, 2016, 26906, 780, 101663],
 [7199, 1731, 28449, 872, 108071]]

ys = [[row[j] for row in ys] for j in range(5)]


fig, ax = plt.subplots(figsize=(5,5))
items = ['Darkeness: No street lighting','Darkness: Street lighting unknown',
             'Darkness: Street lights present and lit', 
             'Darkness: Street lights present but unlit',
             'Daylight: Street light present']



plt.bar(years, 
        #using df['pre_score'] data,
        ys[0], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        label=items[0]) 

plt.bar(years, 
        #using df['pre_score'] data,
        ys[1], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#F78F1E', 
        # with label the first value in first_name
        label=items[2]) 

plt.bar(years, 
        #using df['pre_score'] data,
        ys[2], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#FFC222', 
        # with label the first value in first_name
        label=items[3]) 

ax.set_xticks([p + 1.5 * width for p in range(len(years))])

plt.xlim(min(range(len(years)))-width, max(range(len(years)))+width*4)




ax.set_xticklabels(items[0:3])

plt.legend(items[0:3])


#plt.xlim(min(range(len(years)))-width, max(range(len(years)))+width*4)

plt.show()
