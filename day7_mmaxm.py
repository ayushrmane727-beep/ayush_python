import pandas as pd
data = {
    "name":["Ayush","Tejas","Krushna","Rohan","Sai"],
    "age":[20,21,5,22,19],
    "marks":[80,90,99,70,85],
    "city":["Mumbai","Nashik","Pune","Mumbai","Pune"]
}
df = pd.DataFrame(data)
mumbai = df[df["city"]=="Mumbai"]   # it filters only mumbai row
top = mumbai.sort_values("marks",ascending=False).iloc[0]
print(top)



