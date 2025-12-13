import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sales =[200,300,250,400,500]
plt.plot(days,sales)
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.show()

names =["Ayush","Rohan","Tejas"]
marks =[80,90,75]
 
plt.bar(names,marks)
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title("Marks Comparison")
plt.show()

age =[20,21,22,23,24]
salary =[20000,25000,30000,35000,40000]
plt.scatter(age,salary)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")
plt.show()

marks = [45,55,60,70,80,85,90,95,100]
plt.hist(marks, bins=5)
plt.xlabel("Marks")
plt.xlabel("Students Count")
plt.title("Marks Distribution")
plt.show()
