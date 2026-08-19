#save file

import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,25]

plt.plot(x,y,color='blue',marker='o')
plt.title('simple line plot')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.savefig('line_plot.pdf',dpi=300,bbox_inches='tight')
plt.show()