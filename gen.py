import string
import random

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected. Please include at least one character set.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password


if __name__ =="__main__":

    print("WELCOME TO PASSWORD GENERATOR!")
    length = int(input("Enter password length:\n"))
    # Convert the user input to lowercase and check if it's equal to "yes" if it is then it returns TRUE else FALSE
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    include_digits = input("Include digits? (yes/no): ").lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)

    if password:
        print("\nYour password is:")
        print(password)
        print("THANK YOU!")
   
    



