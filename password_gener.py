import string
import random

def generate_password(length=12):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + punctuation

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    # Generate a password with the default length
    default_length = 12
    password = generate_password(default_length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
