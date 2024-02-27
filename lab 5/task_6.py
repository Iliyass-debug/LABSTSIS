import re

def replace_characters(input_string):
    pattern = re.compile(r'[ ,.]')  
    replaced_string = re.sub(pattern, ':', input_string)

    print(f'Original string: {input_string}')
    print(f'Replaced string: {replaced_string}')

input_string = input("Enter a string: ")
replace_characters(input_string)