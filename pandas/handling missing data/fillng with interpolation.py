import pandas as pd


data = {
    "Name": ["shubham","vedansh", "hindavi"],
    "Age": [10, None, 30],
    "Salary":[50000,None,60000]
}

df=pd.DataFrame(data)
print(df)

df.interpolate(method="linear",axis=0,inplace=True)   #the interpolate will fil the missing vale with liear method.
print(df)                                        # methods like linear,polynomial,time etc
  