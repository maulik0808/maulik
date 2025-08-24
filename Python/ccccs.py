from itertools import permutations
from itertools import combinations 

data=[1,2,3,4,5,6]

result=list(permutations(data,3))

print(result)

print(len(result))

resultt = list(combinations(data,3))

print(resultt)

print(len(resultt))

