import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user preferences
    length = int(input("Enter the desired password length (minimum 8): "))
    while length < 8:
        print("Password length must be at least 8.")
        length = int(input("Enter the desired password length (minimum 8): "))

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

    # Generate password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
