import pandas as pd


data = {
    "Name": ["shubham", None, "hindavi"],
    "Age": [10, None, 30],
    "City": ["nanded", None, "pune"],
    "Salary":[50000,None,60000]
}

df=pd.DataFrame(data)
print(df)

df.fillna(100,inplace=True)
print(df)