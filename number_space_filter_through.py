input_string = "Hela1lo|123|World! 142|45.6e-3|-7.8E2 90 e90e"
cleaned_list = [num for num in ''.join(char if char.isdigit() or char in ' +-.eE' else ' ' for char in input_string).split() if num.count('e') in [0, 1] and num.count('E') in [0, 1] and not (num.startswith('e') or num.startswith('E'))]
print(cleaned_list)
