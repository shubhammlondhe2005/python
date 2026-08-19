#scatter plot for 1 data

import matplotlib.pyplot as plt

hours_studies=[1,2,3,4,5,6,7,8]
exam_score=[50,55,60,65,70,75,80,85]

plt.scatter(hours_studies,exam_score,color='red',marker='^',label='student data')

plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.title('Relation between study time and exam score')
plt.legend()
plt.grid(True)
plt.show()