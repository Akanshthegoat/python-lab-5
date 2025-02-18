string = input("Enter a string: ")

if len(string) < 2:
    print("")
else:
    result = string[:2] + string[-2:]
    print("Resulting string:", result)
