def calculate_permutations(word):
    # Calculate the factorial of the length of the word
    factorial = 1
    for i in range(1, len(word)):
        factorial *= i

    return factorial

# Define the word to compute permutation count
word = "ALGEBRA"

# Calculate and print the permutation count
print(calculate_permutations(word))