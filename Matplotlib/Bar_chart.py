#Bar charts
import matplotlib.pyplot as plt

product=['A','B','C','D']
Sales=[1000,1500,800,1200]
plt.barh(product,Sales,color='orange',label='Sales 2025')
plt.xlabel('product')
plt.ylabel('sales')
plt.title('product sales comparison')
plt.legend()
plt.show()