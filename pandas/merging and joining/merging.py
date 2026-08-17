import pandas as pd

df_customers=pd.DataFrame({
    "Customer_ID":[1,2,3],
    "Name":["Ramesh","suresh","kalpesh"]
})

df_Orders=pd.DataFrame({
    "Customer_ID":[1,2,4],
    "OrderAmount":[250,450,350]
})

df_merged=pd.merge(df_customers,df_Orders,on="Customer_ID",how="inner")
print(df_merged)


'''
1df=m rows
2df=n rows
m*n rows
'''
