import pandas as pd
'''concat is the used to combine or merge the two data sets'''

df_region=pd.DataFrame({
    "Customer_ID":[1,2,3],
    "Name":['shubham','pratik','chandu']
    })

df_region1=pd.DataFrame({
    "Customer_ID":[4,5],
    "Name":['hindavi','vedansh']
})

df_concat=pd.concat([df_region,df_region1],axis=0,ignore_index=True)
print(df_concat)