import re

def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')  
    matches = pattern.findall(input_string)

    if matches:
        print(f'Sequences found: {", ".join(matches)}')
    else:
        print('No matching sequences found.')

input_string = input("Enter a string: ")
find_sequences(input_string)