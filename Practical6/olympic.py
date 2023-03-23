#create a list of the cost
#print the list
cost=[1, 8, 15, 7, 5, 14, 43, 40]
print(cost)
#learn from https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_la$
import matplotlib.pyplot as plt
import numpy as np
N=8
cost = (1, 8, 15, 7, 5, 14, 43, 40)
ind=np.arange(N)
width=0.4
pl=plt.bar(ind, cost, width)
plt.ylable='cost'
plt.title('Olympic Costs')
plt.xticks(ind, ('1984', '1988', '1992', '1996', '2000', '2003', '2008', '2012'$
plt.yticks(np.arange(0, 45, 5))
plt.show()
