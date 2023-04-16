n_terms = int(input("How many terms of the Fibonacci sequence would you like to generate? "))

# initialize the first two terms of the sequence
fibonacci_sequence = [0, 1]

# generate subsequent terms of the sequence
for i in range(2, n_terms):
    next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_term)

# print the sequence
print(f"The first {n_terms} terms of the Fibonacci sequence are: {fibonacci_sequence}")
