# # input_str='i:6 2 2 0 90 0 v:1 2 3 0 0 0 c:1 2 7 0 4 0'
# input_str = "    Ine:6 2 2.0000 0 90.0     0                                      Vasdfa:   1 2.0 3 1 0 0               cOccc:1 23.0 711 0 4 0aaaaaaa"
# input_str = ' '.join([ (w[0].lower() + ':' + ' '.join(input_str.split(w + ':',1)[1].split()[:6])) for w in [word.split(':')[0] for word in input_str.split() if ':' in word] ])

# result = ' '.join([s.split(':',1)[1] for s in sorted([seg for seg in input_str.replace('c:', '|c:').replace('i:', '|i:').replace('v:', '|v:').split('|') if seg], key=lambda x: ['c:', 'i:', 'v:'].index(x.split(':',1)[0] + ':'))])

# print(f"output: '{result}'")

# output: '1 23.0 711 0 4 0aaaaaaa 6 2 2.0000 0 90.0 0 1 2.0 3 1 0 0'


# Input string
input_str = "    Ine:6 2 2.0000f 0 90.0f     0                                      Vasdffa:   1 2.0 3 1 0 0ff               cOccc:1 23.0 711 0 4 0aaaaaaa"
# input_str = '1 23.0 711 0 4 6 2 2.0000 0 90.0 0 1 2.0 3 1 0 0'
# Step 1: Convert prefixes to single letters
input_str = ' '.join([w[0].lower() + ':' + ' '.join(input_str.split(w + ':',1)[1].split()[:6]) 
                     for w in [word.split(':')[0] for word in input_str.split() if ':' in word]])
print(f"input_str: '{input_str}'")

# Step 2 & 3: Sort segments and concatenate numerical data
# result = ' '.join([s.split(':',1)[1].strip() 
#                    for s in sorted([seg.strip() for seg in input_str.replace('c:', '|c:').replace('i:', '|i:').replace('v:', '|v:').split('|') if seg.strip()], 
#                                    key=lambda x: ['c:', 'i:', 'v:'].index(x.split(':',1)[0] + ':'))])

result = [item for s in sorted([seg.strip() for seg in input_str.replace('c:', '|c:').replace('i:', '|i:').replace('v:', '|v:').split('|') if seg.strip()], key=lambda x: ['c:', 'i:', 'v:'].index(x.split(':',1)[0] + ':')) for item in s.split(':',1)[1].split()]


# Output the result
print(f"output: '{result}'")


