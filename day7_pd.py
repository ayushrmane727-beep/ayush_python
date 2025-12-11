import pandas as pd
S = pd.Series([5,10,15,20])
data= {
    "name":["Ayush","tejas","krushna"],
    "age":[20,21,5],
    "marks":[80,90,99]
    }
df = pd.DataFrame(data)
print(df["name"])
print(df[df["age"]>18])
df["passed"]=["passed","passed","passed"]
print(df.sort_values("marks"))
print(df)
print(df.loc[0:1])
df=df.drop("age",axis=1)
print(df)
print(df.describe())
