import random

print("Welcome to the PyPassword Generator!")

number_letters = int(input("How many letters would you like in your password?\n"))

number_symbols = int(input("How many symbols would you like?\n"))

number_numbers = int(input("How many numbers would you like?\n"))

list_letters = [];
list_numbers = [];
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'];

for i in range(97, 123):
    list_letters.append(chr(i))

for i in range(65, 91):
    list_letters.append(chr(i))

for i in range(48, 58):
    list_numbers.append(chr(i))

password = []

for i in range(0, number_letters):
    password.append(random.choice(list_letters))

for i in range(0, number_numbers):
    password.append(random.choice(list_numbers))

for i in range(0, number_symbols):
    password.append(random.choice(list_symbols))

print(password)

random.shuffle(password)

print(password)

your_password = ""

for char in password:
    your_password += char

print(your_password)
