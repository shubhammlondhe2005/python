import pandas as pd


data = {
    "Name": ["shubham", None, "hindavi"],
    "Age": [10, None, 30],
    "City": ["nanded", None, "pune"],
    "Salary":[50000,None,60000]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())      #true means the datat is missing here

print(df.isnull().sum())    #it will show the how much values are null