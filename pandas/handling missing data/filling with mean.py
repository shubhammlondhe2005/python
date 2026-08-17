import pandas as pd


data = {
    "Name": ["shubham", None, "hindavi"],     #filling mean will work on the numerical data or continues data not categorical data
    "Age": [10, None, 30],
    "City": ["nanded", None, "pune"],
    "Salary":[50000,None,60000]
}

df=pd.DataFrame(data)
print(df)

df["Age"].fillna(df["Age"].mean(),inplace=True) #it will give the mean of the Age

df["Salary"].fillna(df["Salary"].mean(),inplace=True) #it will give the mean of the Salary
print(df)


df["Name"].fillna(df["Name"].mean(),inplace=True)
print(df)

#''''it will give the Error as Name have the categorical data not numerical''''
