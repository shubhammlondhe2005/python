import pandas as pd

data = {
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
    ]
}

df=pd.DataFrame(data)
print(df.describe())