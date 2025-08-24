from itertools import permutations
from itertools import combinations

list_word =["sales","exclusive","limited","offer"]

result=list(permutations(list_word,4))

print(result)

print(len(result))


result_data=list(combinations(list_word,4))

print(result)

print(len(result))