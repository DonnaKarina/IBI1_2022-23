#create a list of the cost
#print the list
#learn from https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_la$
cost=[1, 8, 15, 7, 5, 14, 43, 40]
year=['1984', '1988', '1992', '1996', '2000', '2003', '2008', '2012']
import numpy
year=numpy.array(year)
cost=numpy.array(cost)
sortedcost=cost.argsort()
sorted_year=year[sortedcost]
sorted_cost=cost[sortedcost]
print(sorted_cost)
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
width=0.4
ax.bar(sorted_year, sorted_cost, width)
plt.ylable='cost'
ax.set_title('Olympic Costs')
plt.yticks(np.arange(0, 45, 5))
plt.show()
