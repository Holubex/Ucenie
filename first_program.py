import random

# Zoznam pismen,čísel a symbolov

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '.', '>', '<', ':']

print('Vitajte v programe na generovanie hesla.')

number_of_letters = int(input(f'Koľko písmen má obsahovať heslo?\n'))
number_of_symbols = int(input(f'Koľko znakov má obsahovať heslo?\n'))
number_of_numbers = int(input(f'Koľko čísiel má obsahovať heslo?\n'))

# Vytvorenie hesla
password_list = []

for letter in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbols))

for number in range(1, number_of_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

# premena password_list na string
password = ""
for char in password_list:
    password += char
print("char", char)

password_final = ''.join(password_list)
print(f'Your password is: {password_final}')

