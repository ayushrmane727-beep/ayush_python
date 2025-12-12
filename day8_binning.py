import pandas as pd
import numpy as np
data ={
    "name":["Ayush","Rohan","Sara",None,"Mira"],
    "age":[21,22,None,25,23],
    "salary":[50000,None,45000,52000,None],
    "city":["Mumbai","pune","Mumbai","pune",None]
}
df= pd.DataFrame(data)
bins =[0,40000,50000,60000]
labels =["Lows","Medium","High"]
df["salary_bins"]=pd.cut(df["salary"],bins=bins,labels=labels)
print(df)