# 1.Employee tables
import pandas as pd

emp = pd.DataFrame({
    'EMPNO':['E101','E102','E103','E105','E106'],
    'NAME':['Vivek','Vishal','Priyal','Shrushti','Pranay'],
    'DEPT':['R&D','Marketing','Product','Product','Product'],
    'SALARY':[145000,90000,120000,80000,100000],
    'BRANCH':['Nagpur','Pune','Bangalore','Nagpur','Mumbai']
})

desig = pd.DataFrame({
    'EMPNO':['E101','E102','E103','E105','E106'],
    'DESIGNATION':['Project Manager','Sales Manager','Design Architect','Software Dev','Project Lead']
})

# Merge tables
df = pd.merge(emp, desig, on='EMPNO')

print(df)

# Example operations
print("\nEmployees in Nagpur:\n", df[df['BRANCH']=='Nagpur'])
print("\nHighest Salary:\n", df.loc[df['SALARY'].idxmax()])


# 2.Supplier Details Table
import pandas as pd

items = pd.DataFrame({
    'ITEM_ID':['C101','C102','C103','C104','C105'],
    'ITEM_NAME':['Jeans','Shirt','Saree','Sweater','Tshirt'],
    'CATEGORY':['Bottomwear','Topwear','Ethnic','Winter','Active'],
    'PRICE':[1500,1200,5000,2000,800],
    'STOCK':[30,50,20,15,60],
    'SUPPLIER':['Levis','Raymond','Fabindia','Spark','Nike']
})

suppliers = pd.DataFrame({
    'SUPPLIER':['Levis','Raymond','Fabindia','Spark','Nike'],
    'LOCATION':['Mumbai','Delhi','Bangalore','Chandigarh','Pune']
})

print("\nAll Items:\n", items)

# Merge
df = pd.merge(items, suppliers, on='SUPPLIER')

print("\nMerged Data:\n", df)

print("\nItems with low stock (<20):\n", df[df['STOCK'] < 20])
print("\nCostliest Item:\n", df.loc[df['PRICE'].idxmax()]