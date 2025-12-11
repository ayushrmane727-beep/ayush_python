import pandas as pd
data = {
    "name":["Ayush","Tejas","Krushna","Rohan","Sai"],
    "age":[20,21,5,22,19],
    "marks":[80,90,99,70,85],
    "city":["Mumbai","Nashik","Pune","Mumbai","Pune"]
}
df = pd.DataFrame(data)
extra ={
    "name":["Ayush","tejas","kruhsna"],
    "sport":["cricket","chess","football"]
}
df2=pd.DataFrame(extra)
merged=pd.merge(df,df2,on="name",how="left")
merged["sport"]=merged["sport"].fillna("no sport")
print(merged)
