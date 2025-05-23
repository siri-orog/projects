import random
import string

# Function to Generate Password
def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    character_pool = ""
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character set selected."

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# User Input
length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and Display Password
generated_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
print(f"Generated Password: {generated_password}")