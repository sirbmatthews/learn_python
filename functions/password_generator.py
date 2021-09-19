#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '}', '{', '-', '/', '|']

def generate_password(password_length):
	"""Generates a password using the provided password length"""
	password = ""
	nr_letters = random.randint(int(round(password_length/2)), password_length - 2)
	nr_symbols = random.randint(1, int(round((password_length - nr_letters)/2)))
	nr_numbers = password_length - nr_letters - nr_symbols

	for _ in range(0, nr_letters):
		password += random.choice(letters)

	for _ in range(0, nr_symbols):
		password += random.choice(symbols)

	for _ in range(0, nr_numbers):
		password += random.choice(numbers)

	password = ''.join(random.sample(password, len(password)))  
	return password