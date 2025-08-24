import numpy as np
import pandas as pd

data = 'forestfires.csv'

df = pd.read_csv(data)

df.head()

fires =df.iloc[:5,8:]

print(fires)

a =np.array([1,2,3])

print(a)

n1 = np.array(fires[:1])

print(n1)

b = np.array([[1,2],[3,4]])

print(b)

n2 =np.array(fires[:2],dtype =int)

print(n2)

c= np.array ([[1,2],[3,4],[5,6]])

print(c)

n3 = np.array(fires[:3], dtype = int)

print(n3)

d = np.array([1,2,3,4,5], ndim = 2)

print(d)

e = np.array([1,2,3],dtype =complex)

print(e)


dt = np.dtype(np.int32)

print(dt)

dt = np.dtype(('age',np.int8))

print(dt)

dt = np.dtype(('age',np.int8))
a1 =np.array([(10,),(20,),(30,)],dytpe =dt)

print(a1)

dt = np.dtype([('age',np.int8)])

a1 = np.array([(10,),(20,),(30,)],dtype =dt)

print(a1['age'])

student = np.dtype([('name','s20'),('age','i1'),('marks','f4')])

print(student)

a2 = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 

print(a2)


x1 = np.array([[1,2,3]])

x7 = np.array([2,3,4])
x7
x7.dtype

x8 =np.array([1.2,3.5,5.1])
x8.dtype

x9 =np.empty([2,3],dtype =int)

print(x9)

x10 = np.zeros(5)
print(x10)

x11 = np.zeros((5,),dtype = np.int)

print(x11)

x12 = np.ones(5)

print(x12)

x13 = np.ones([2,2], dtype =int)

print(x13)

x14 = np.arange(10,20,2)
print(x14)

x15 = np.arange(10,20,0.5)

print(x15)

x16 = np.linspace(2.0,4.0,num=5)
print(x16)

x17 = np.linspace(2.0,4.0, num= 5, endpoint= False)

print(x17)

u1 =[1,2,3]

v1 = np.asarray(u1)

print(v1)

u1 =[1,2,3]

v1=np.asarray(u1, dtype = float)


print(v1)

u2 = (1,2,3)
v2 =np.asarray(u2)
print(v2)

u3 = [(1,2,3),(4,5)]

v3 = np.asarray(u3)

print(v3)

y1 = np.arange(5)

print(y1)

y1 = np.arange(5, dtype = float)

print(y1)

y1 = np.arange(10,20,2)

print(y1)

y2 = np.linspace(10,20,5)

print(y2)

y2 = np.linspace(10,20,5, endpoint = False)

print(y2)

import numpy as np
arr_2d =np.array([[1,2,3],[4,5,6],[7,8,9]])

sum_axis_0 = np.sum(arr_2d, axis =1)

print(sum_axis_0)

import numpy as np

n3 = np.random.randint(1,15, size = (3,5))

print(n3)


x18 = np.arange(10)

print(x18)

s = slice(2,7,2)

print(x18[s])

x20 = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(x20)

print(x20[1:])

print(x20[...,1])

print(x20[1,...])

print(x20[...,1:])

print(x20[:1,...])

l1 =np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])

l2 =np.array([1.0,2.0,3.0])
print('First array :')

print(l1)

print('\n')

print("the first dimension of arary is {}". format(l1.ndim))

print('\n')
print('second array :')

print(l2)

print('\n')

print("the second dimension of array is{}". format(l2. ndim))


arr = np.random.randint(0,256, size = (4,4,3), dtype=np.uint8)

print(arr)

arr1 = np.random.randint(0,256, size=(10,4,4,3), dtype=np.uint8)

print(arr1)


