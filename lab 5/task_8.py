def split_at_uppercase(input_string):
    split_string = [char if char.islower() else ' ' + char for char in input_string]
    result = ''.join(split_string).split()

    return result


input_string = input("Enter a string: ")
result = split_at_uppercase(input_string)
print(f'Split result: {result}')
