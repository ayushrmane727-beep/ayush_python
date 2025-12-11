import pandas as pd
data = {
    "name":["Ayush","Tejas","Krushna","Rohan","Sai"],
    "age":[20,21,5,22,19],
    "marks":[80,90,99,70,85],
    "city":["Mumbai","Nashik","Pune","Mumbai","Pune"]
}
df = pd.DataFrame(data)
print(df[(df["marks"]>= 80) &(df["marks"]<=90)])