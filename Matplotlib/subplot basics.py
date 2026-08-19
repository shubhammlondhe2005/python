#subplot basics

import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,25]

plt.subplot(1,2,1)  #1 row,2 column,1st subplot
plt.plot(x,y)
plt.title('Line chart')

plt.subplot(1,2,2)  #1 row,2 column,2st subplot
plt.bar(x,y)
plt.title('bar chart')

plt.tight_layout()
plt.show()