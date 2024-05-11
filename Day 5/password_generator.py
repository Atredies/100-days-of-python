import random

print("Welcome to PyPassowrd Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_letters = int(input("How many letters? \n"))

number_of_symbols = int(input("How many symbols? \n"))

number_of_numbers = int(input("How many numbers? \n"))

password = ""

print(len(numbers))

for i in range (0, number_of_letters):
    password += letters[random.randint(0,int(len(letters))) -1]

for i in range (0, number_of_symbols):
    password += symbols[random.randint(0,int(len(symbols))) -1]

for i in range (0, number_of_numbers):
    password += numbers[random.randint(0,int(len(numbers))) -1]

# Password shuffler
pass_list = list(password)
random.shuffle(pass_list)

shuffled_pass = ""
for i in pass_list:
    shuffled_pass += i

print("Here is your password: " + shuffled_pass)