#create a list of the cost 
#print the list
cost=[1, 8, 15, 7, 5, 14, 43, 40]
print(cost)
#learn from https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html#sphx-glr-gallery-lines-bars-and-markers-bar-label-demo-py 
import matplotlib.pyplot as plt
import numpy as np
Year = ['1984', '1988', '1992', '1996', '2000', '2003', '2008', '2012']
cost = [1, 8, 15, 7, 5, 14, 43, 40]
fig, ax = plt.subplots()
bar_container = ax.bar(Year, cost)
ax.set(ylabel='cost', title='Olympic Costs', ylim=(0,45))
ax.bar_label(bar_container, fmt='{:,.0f}')
plt.show()
