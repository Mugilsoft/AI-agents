import math
# filename: perm_calc.py

word = "ALGEBRA"
lowercase_word = ''.join(filter(str.isalpha, word)).lower()

total_chars = len(lowercase_word)
num_a = lowercase_word.count('a')
num_g = lowercase_word.count('g')
num_e = lowercase_word.count('e')
num_l = lowercase_word.count('l')
num_b = lowercase_word.count('b')
num_r = lowercase_word.count('r')

denominator = math.factorial(total_chars)

print(denominator // (math.factorial(num_a) * math.factorial(num_g) * math.factorial(num_e) * math.factorial(num_l) * math.factorial(num_b) * math.factorial(num_r)))