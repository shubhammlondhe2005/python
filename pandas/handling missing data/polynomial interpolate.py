import pandas as pd

data = {
    "Name": ["shubham", "vedansh", "hindavi", "rahul", "pratik"],
    "Age": [10, 15, None, 25, 30],
    "Salary": [30000, 40000, None, 60000, 70000]
}

df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Polynomial interpolation
df.interpolate(
    method="polynomial",
    order=2,
    axis=0,
    inplace=True
)

# Print the DataFrame after polynomial interpolation
print("\nDataFrame after Polynomial Interpolation:")
print(df)