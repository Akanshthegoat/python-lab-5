string = input("Enter a string: ")

if len(string) > 1:
    string = string[0] + string[1:].replace(string[0], '$')

print("Modified string:", string)
