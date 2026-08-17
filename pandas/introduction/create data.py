import pandas as pd

data = {
    "Name": ["shubham", "vedansh", "hindavi"],
    "Age": [10, 20, 30],
    "City": ["nanded", "mumbai", "pune"]
}

df = pd.DataFrame(data)

print(df)

df.to_csv("my_data.csv", index=False)