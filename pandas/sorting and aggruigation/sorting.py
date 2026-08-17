import pandas as pd

data={
    
    "Name":["Arun","varun","karun"],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]
    
}

df=pd.DataFrame(data)
print(df)

df.sort_values(by="Age",ascending=True,inplace=True,ignore_index=True)     #here the values of the Age is sorted by the ascending order and the ignore idex is written for the ignoring the index of the output.
print(df)