import pandas as pd 
import matplotlib.pyplot as plt 
data ={
    "city":["Mumbai","Pune","Mumbai","Pune","Mumbai"],
    "salary":[50000,45000,60000,52000,58000]
}
df=pd.DataFrame(data)
city_avg =df.groupby("city")["salary"].mean()

city_avg.plot(kind="bar")
plt.title("Average Salary by City")
plt.ylabel("Salary")
plt.show()
