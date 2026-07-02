import math

word = "ALGEBRA"
n = len(word)

# Count occurrences of each character
from collections import Counter
char_counts = Counter(word)

# Calculate the denominator for repeated characters
denominator = 1
for count in char_counts.values():
    denominator *= math.factorial(count)

# Calculate the total number of permutations
num_permutations = math.factorial(n) / denominator

print(f"The word is: {word}")
print(f"Total letters (n): {n}")
print(f"Character counts: {char_counts}")
print(f"Number of unique permutations: {int(num_permutations)}")