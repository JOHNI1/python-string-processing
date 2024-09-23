
input_str = """[1][2][3]"""


result = [segment.replace('[', '').strip() for segment in input_str.split(']') if segment.strip()]

print(result)