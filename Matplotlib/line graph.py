#use of plt
import matplotlib.pyplot as plt

months=[1,2,3,4]
Sales=[1000,1500,1200,1800]

plt.plot(months,Sales,color='blue',linestyle='--',linewidth=2,marker='o',label='2025 sales data')
plt.xlabel('Months')
plt.ylabel('Sales per months')
plt.title('Monthly sales data report')
plt.legend(loc='lower right',fontsize=15)
plt.grid(color='gray',linestyle='-',linewidth=1)
plt.xlim(1,5)
plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
plt.show()
