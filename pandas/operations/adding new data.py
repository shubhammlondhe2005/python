import pandas as pd


data = {
    "Name": ["shubham", "vedansh", "hindavi"],
    "Age": [10, 20, 30],
    "City": ["nanded", "mumbai", "pune"],
    "Salary":[50000,45000,60000]
}

df = pd.DataFrame(data)

print(df)

df["bonus"]=df["Salary"]*0.10  #it will add the new column
print(df)