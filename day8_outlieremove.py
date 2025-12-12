import pandas as pd
import numpy as np
data ={
    "name":["Ayush","Rohan","Sara",None,"Mira"],
    "age":[21,22,None,25,23],
    "salary":[50000,None,45000,52000,None],
    "city":["Mumbai","pune","Mumbai","pune",None]
}
df= pd.DataFrame(data)
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_no_outliers = df[(df["salary"] > lower) & (df["salary"] < upper)]
print(df_no_outliers)