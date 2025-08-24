from itertools import combinations
from itertools import permutations

team_data=[1,2,3,4,5,6,7,8,9,10]

result =list(permutations(team_data,4))

print(result)

print(len(result))
result_data=list(combinations(team_data,4))

print(result_data)
print(len(result_data))