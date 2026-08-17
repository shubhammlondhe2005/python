import pandas as pd

data = {
    "ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115
    ],

    "Name": [
        "shubham", "vedansh", "hindavi", "rahul", "pratik",
        "rohan", "akshay", "sneha", "pooja", "neha",
        "amit", "sachin", "om", "aditya", "viraj"
    ],

    "Age": [
        20, 21, 20, 22, 21,
        23, 22, 20, 23, 21,
        22, 24, 23, 20, 24
    ],

    "City": [
        "nanded", "mumbai", "pune", "nagpur", "nashik",
        "pune", "mumbai", "nanded", "pune", "nagpur",
        "nashik", "pune", "mumbai", "nanded", "pune"
    ],

    "Salary": [
        30000, 35000, 40000, 45000, 32000,
        50000, 42000, 38000, 55000, 36000,
        48000, 52000, 46000, 34000, 60000
    ]
}

df = pd.DataFrame(data)

print(df)

grouped=df.groupby("Age")["Salary"].sum()
print(grouped)                                    #here we hve done the group by the help of the Age and the salary
                                
grouped2=df.groupby(["Age","Name"])["Salary"].sum()
print(grouped2)                                              

''' common group by
 1-sum()
 2-mean()
 3-count()
 4-min()
 5-max()
 6-std()'''