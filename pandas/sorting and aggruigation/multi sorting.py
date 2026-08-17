import pandas as pd

data={
    
    "Name":["Arun","varun","karun"],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]
    
}

df=pd.DataFrame(data)
print(df)

df.sort_values(by=["Age","Salary"],
               ascending=[True,False],
               inplace=True,
               ignore_index=True)

print(df)
