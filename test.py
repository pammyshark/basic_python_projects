import string
import random

print("Welcome to the PyPassword generator!")
letters = int(input("How many letters would you like in your password?"))
symbols = int(input("How many symbols would you like in your password?"))
numbers = int(input("How many numbers would you like in your password"))
print("Your password is:")

# importing and saving libraries
letter_options = string.ascii_letters
symbol_options = string.punctuation
number_options = string.digits

# generating password elements according inputs
letters_random = random.choices(letter_options, k = letters)
symbol_random = random.choices(symbol_options, k = symbols)
number_options = random.choices(number_options, k = numbers)

# setting up the password
password = letters_random + symbol_random + number_options
random.shuffle(password)
password = "".join(password)
print(password)
