import pandas as pd

data={
    
    "Name":["Arun","varun","karun"],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]
    
}

df=pd.DataFrame(data)
print(df)

avg_salary=df["Salary"].mean()
print(avg_salary)