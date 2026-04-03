# 1.Cosmetic company
import matplotlib.pyplot as plt
months = list(range(1,13))
profit = [100,200,150,300,250,400,350,450,300,200,100,500]

# Line Plot
plt.plot(months, profit)
plt.title("Total Profit")
plt.xlabel("Months")
plt.ylabel("Profit")
plt.show()

# Multiline Plot
facecream = [50,60,70,80,90,100,110,120,130,140,150,160]
facewash = [30,40,50,60,70,80,90,100,110,120,130,140]

plt.plot(months, facecream, label="Face Cream")
plt.plot(months, facewash, label="Face Wash")
plt.legend()
plt.show()

# Bar Chart
plt.bar(months, facecream)
plt.title("Face Cream Sales")
plt.show()

# Pie Chart
products = ['Cream','Wash']
sales = [sum(facecream), sum(facewash)]

plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.show()


# 2. Recruitments Companies

import matplotlib.pyplot as plt

companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Amdocs']
recruits = [120,150,180,90,110,80]

# Bar Chart
plt.bar(companies, recruits)
plt.title("Recruitment Data")
plt.show()

# Pie Chart
plt.pie(recruits, labels=companies, autopct='%1.1f%%')
plt.show()

# Doughnut Chart
plt.pie(recruits, labels=companies, wedgeprops={'width':0.4})
plt.show()

# Comparison IBM vs Amdocs
plt.bar(['IBM','Amdocs'], [90,80])
plt.title("IBM vs Amdocs")
plt.show()