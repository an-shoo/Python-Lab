def count_characters(filename):
    with open(filename, 'r') as file:
        text = file.read()
        upper_case = sum(1 for char in text if char.isupper())
        lower_case = sum(1 for char in text if char.islower())
        digits = sum(1 for char in text if char.isdigit())
    return upper_case, lower_case, digits

filename = 'textfile2.txt'
with open(filename, 'w') as file:
    for _ in range(5):
        line = input("Enter a line of text: ")
        file.write(line + '\n')

upper_case, lower_case, digits = count_characters(filename)
print(f"Upper case letters: {upper_case}")
print(f"Lower case letters: {lower_case}")
print(f"Digits: {digits}")
