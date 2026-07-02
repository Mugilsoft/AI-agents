import math
from collections import Counter

def unique_permutations(word):
    """
    Calculates the number of unique permutations of a given word.
    """
    n = len(word)
    
    # Calculate n!
    numerator = math.factorial(n)
    
    # Count character frequencies
    char_counts = Counter(word)
    
    # Calculate the product of factorials of repeating character counts
    denominator = 1
    for count in char_counts.values():
        denominator *= math.factorial(count)
            
    return numerator // denominator

# Test with the word 'ALGEBRA'
word_to_test = 'ALGEBRA'
result = unique_permutations(word_to_test)
print(result)