#drawing the pie chart
import matplotlib.pyplot as plt

region=['North','South','West','East']
revanue=[3000,2000,1500,1000]

plt.pie(revanue,labels=region,autopct='%1.1f%%',colors=['gold','skyblue','green','red'])
plt.title('revanue contribution by region')
plt.show()