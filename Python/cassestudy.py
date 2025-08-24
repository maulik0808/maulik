import pandas as pd
import numpy as np
data ={
    "date":pd.date_range(start="2024-01-01",periods=20,freq="D"),
    "product":np.random.choice(["laptop","phone","tablet"],size=20),
    "Region":np.random.choice(["north","east","west","south"],size=20),
    "units_sold":np.random.randint(1,20,size=20),
    "unit_price":np.random.randint(200,1500,size=20)
}

df=pd.DataFrame(data)

print(df)
print()
print()

df["revenue"]=df["units_sold"] * df["unit_price"]

print(df.head())

print()

print(df.to_csv("sales.csv",index=True))
df.to_excel("sales.xlsx",index=False,sheet_name="sales Data")

print()

#print(\n Summary Statisctics:)

print(df.describe())

print()

total_revenue = df["revenue"].sum()
print("\n Toatal revenue:", total_revenue)

print()

sales_by_product =df.groupby("product")["revenue"].sum().reset_index()
print("\n sales by product:\n", sales_by_product)

print()

sales_by_region =df.groupby("Region")["revenue"].sum().reset_index()
print("\n sales by region :\n", sales_by_region)