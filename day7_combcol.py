import pandas as pd
data = {
    "name":["Ayush","Tejas","Krushna","Rohan","Sai"],
    "age":[20,21,5,22,19],
    "marks":[80,90,99,70,85],
    "city":["Mumbai","Nashik","Pune","Mumbai","Pune"]
}
df = pd.DataFrame(data)
df["surname"]=["mane","gaynar","waghmare","sable","navadkar"]
df["full_address"]=df["city"]+" "+df["surname"]
print(df)