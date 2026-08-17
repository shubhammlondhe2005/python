import pandas as pd


data = {
    "Name": ["shubham", "vedansh", "hindavi"],
    "Age": [10, 20, 30],
    "City": ["nanded", "mumbai", "pune"],
    "Salary":[50000,45000,60000]
}

df = pd.DataFrame(data)

df.loc[0,"Salary"]=55000    #updatin the only 1 value
print(df)

#df.to_csv("emp_data.csv",index=False)
#df=pd.read_csv(r"C:\Users\lenovo\OneDrive\Desktop\YT New python\pandas\emp_data.csv")