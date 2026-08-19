#scatter plot for 2 data

import matplotlib.pyplot as plt

plt.scatter([1,2,3,4,5],[50,55,60,65,70],color='red',marker='^',label='student data')
plt.scatter([1,2,3,4,5],[55,60,65,70,75],color='blue',marker='^',label='student data')
plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.title('comparison of two classes')
plt.legend()
plt.grid(True)
plt.show()