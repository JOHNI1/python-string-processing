input_str = "1 1 3 0.2 0.3 50000"

# Convert the string into a list of words/numbers
words = input_str.split()

# Repeat the list 3 times, creating new elements
result = [word for word in words] * 3

# Output the result
print(result)

result[3] = 'aaaaaaaaaaaaaaaaaaaaaaaa'

print(result)
