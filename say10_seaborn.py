import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data = {
    "age": [22, 25, 30, 28, 35, 40, 26, 32],
    "salary": [20000, 25000, 40000, 35000, 60000, 70000, 28000, 45000],
    "city": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

sns.histplot(df["salary"],bins=10)#how many employees have higher salary
plt.show()

sns.boxplot(x=df["salary"])#which is extreme value in salary
plt.show()

sns.countplot(x="city",data=df)
plt.show()

sns.scatterplot(x="city",y="salary",data=df)
plt.show()

sns.barplot(x="city",y="salary",data=df)
plt.show()


