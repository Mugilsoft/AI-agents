import math
# filename: perm_calc.py

word = "ALGEBRA"
lowercase_word = ''.join(filter(str.isalpha, word)).lower()

num_unique_permutations = 1
for char in set(lowercase_word):
    num_unique_permutations *= math.factorial(lowercase_word.count(char))

print(num_unique_permutations)