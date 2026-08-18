#drawing the histogram
import matplotlib.pyplot as plt

scores=[45,85,65,32,15,24,65,22,35,62,42,52,36,42,25,21,15]

plt.hist(scores,bins=6,color='skyblue',edgecolor='white',linestyle=':')
plt.xlabel('score range')
plt.ylabel('Number of students')
plt.title('score Distribution of student')
plt.show()