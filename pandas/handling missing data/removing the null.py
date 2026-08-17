import pandas as pd


data = {
    "Name": ["shubham", None, "hindavi"],
    "Age": [10, None, 30],
    "City": ["nanded", None, "pune"],
    "Salary":[50000,None,60000]
}

df = pd.DataFrame(data)
print(df)


df.dropna(axis=0,inplace=True)  #axis 0 for row deletion and the axis 1 for the column deletion 
print(df)                       #dont write the axis for the deleting every value in the table

