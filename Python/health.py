import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales_data =np.array([[2200,2350,2600,2750],[2100,2150,2400,2500],[2000,1950,2100,2200],[2500,2650,2800,2900]])

branch_total = np.sum(sales_data, axis=1)

print("Total sales per branch : ", branch_total)

#highest sales month per each branch

highest_month = np.argmax(sales_data, axis=1)

print("highest month per barch : ", highest_month)

#average of brach
average_month =np.mean(sales_data, axis=0)

print("average month per branch: ", average_month)