import pandas as pd
import numpy as np
data ={
    "name":["Ayush","Rohan","Sara",None,"Mira"],
    "age":[21,22,None,25,23],
    "salary":[50000,None,45000,52000,None],
    "city":["Mumbai","pune","Mumbai","pune",None]
}
df= pd.DataFrame(data)
unique_cities = df["city"].nunique()#only count
print(unique_cities)
unique_cities = df["city"].unique()#which are 
print(unique_cities)
