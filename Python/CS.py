from itertools import combinations
fruits_data =["Apple","Banana","orange","grapes","mango"]

result =list(combinations(fruits_data,3))

print(result)
print(len(result))

from itertools import permutations
fruits_data =["Apple","Banana","orange","grapes","mango"]

result= list(permutations(fruits_data,3))

print(result)

print(len(result))


from itertools import combinations_with_replacement

fruits_data=["Apple","Banana","orange","grapes","mango"]

result=list(combinations_with_replacement(fruits_data,3))

print(result)

print(len(result))
