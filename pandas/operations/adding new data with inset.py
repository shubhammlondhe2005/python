import pandas as pd


data = {
    "Name": ["shubham", "vedansh", "hindavi"],
    "Age": [10, 20, 30],
    "City": ["nanded", "mumbai", "pune"],
    "Salary":[50000,45000,60000]
}

df = pd.DataFrame(data)

print(df)

df.insert(0,"Bonus",df["Salary"]*0.10)  #we can use the insert with the existing column or without it.
print(df)

df.insert(0,"Empl_NO",[10,20,30])  # we can keep the value without the condition direct.
print(df)