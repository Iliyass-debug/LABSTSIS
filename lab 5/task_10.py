def camel_to_snake(camel_case):
    result = [camel_case[0].lower()]

    for char in camel_case[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)

    return ''.join(result)

camel_case_string = input("Enter a camel case string: ")
snake_case_string = camel_to_snake(camel_case_string)
print(f'Snake case string: {snake_case_string}')