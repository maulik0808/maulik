import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = "forestfires.csv"

df = pd.read_csv(data)

print(df.head())
print()
fires = df.iloc[:5,8:]

print(fires)

arr1 = np.array([1,2,3])

print()

print(arr1)

n1 = np.array(fires[:1])

print()

print(n1)

print()

arr2 = np.array([[1,2],[3,4]])

print(arr2)

n2 =np.array(fires[:2])

print()

print(n2)

print()
arr3 =np.array([[1,2],[3,4],[5,6]])

print(arr3)
n3 = np.array(fires[:3])

print()

print(n3)

result_array = arr3.reshape(3,2)

print(result_array)

print()

result_array= arr3.reshape(2,3)

print(result_array)

print(result_array)

print()

reshaped_array1 == arr1.reshape(3,1)

print(reshaped_array1)