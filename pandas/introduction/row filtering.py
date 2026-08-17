import pandas as pd

data = {
    "ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115,
        116, 117, 118, 119, 120,
        121, 122, 123, 124, 125,
        126, 127, 128, 129, 130,
        131, 132, 133, 134, 135,
        136, 137, 138, 139, 140
    ],

    "Name": [
        "shubham", "vedansh", "hindavi", "rahul", "pratik",
        "rohan", "akshay", "sneha", "pooja", "neha",
        "amit", "sachin", "om", "aditya", "viraj",
        "tejas", "kunal", "aniket", "nikhil", "saurabh",
        "tanvi", "sakshi", "riya", "isha", "simran",
        "pranav", "atharva", "yash", "harsh", "manish",
        "vishal", "rohit", "mayur", "gaurav", "karan",
        "varun", "mohit", "ajay", "deepak", "abhishek"
    ],

    "Age": [
        21, 22, 20, 23, 21,
        24, 22, 20, 23, 21,
        25, 24, 22, 20, 23,
        21, 26, 22, 24, 23,
        20, 21, 22, 24, 23,
        21, 20, 22, 25, 24,
        23, 21, 26, 22, 24,
        23, 25, 21, 27, 22
    ],

    "City": [
        "nanded", "mumbai", "pune", "nagpur", "nashik",
        "kolhapur", "aurangabad", "satara", "solapur", "thane",
        "pune", "mumbai", "nanded", "nagpur", "nashik",
        "pune", "kolhapur", "satara", "solapur", "thane",
        "mumbai", "pune", "nagpur", "nashik", "nanded",
        "aurangabad", "pune", "mumbai", "kolhapur", "nagpur",
        "nashik", "satara", "solapur", "thane", "pune",
        "nanded", "mumbai", "nagpur", "nashik", "pune"
    ],

    "Salary": [
        25000, 32000, 28000, 35000, 30000,
        42000, 38000, 27000, 33000, 29000,
        45000, 40000, 31000, 36000, 39000,
        34000, 48000, 37000, 41000, 43000,
        26000, 30000, 35000, 28000, 32000,
        38000, 45000, 40000, 36000, 42000,
        33000, 39000, 47000, 35000, 44000,
        31000, 46000, 29000, 50000, 37000
    ]
}

df=pd.DataFrame(data)

filt=df[df["Salary"]>40000]    # thise comdition is for the single condition
print(filt)

fil=df[df["Name"]=="shubham"]    # thise comdition is for the single condition
print(fil)


filt1=df[(df["Age"]>20) & (df["Salary"]>39000)] # here the AND conditions are applied
print(filt1)

filt2=df[(df["Age"]>20) | (df["Salary"]>39000)]  #herer the OR condition is applied
print(filt2)

