import random
import string

def generate_password(length, include_upper, include_lower, include_numbers, include_symbols):
    chars = ''
    if include_upper:
        chars += string.ascii_uppercase
    if include_lower:
        chars += string.ascii_lowercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    if not chars:
        print("Please select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    while True:
        length = input("Enter password length: ")
        if not length.isdigit():
            print("Invalid input. Please enter a valid number for password length.")
            continue
        length = int(length)

        include_upper = input("Include uppercase letters? (y/n): ").lower()
        if include_upper not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            choice = input("Press 'c' to continue or 'x' to exit: ").lower()
            if choice == 'x':
                break
            else:
                continue
        include_upper = include_upper == 'y'

        include_lower = input("Include lowercase letters? (y/n): ").lower()
        if include_lower not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            choice = input("Press 'c' to continue or 'x' to exit: ").lower()
            if choice == 'x':
                break
            else:
                continue
        include_lower = include_lower == 'y'

        include_numbers = input("Include numbers? (y/n): ").lower()
        if include_numbers not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            choice = input("Press 'c' to continue or 'x' to exit: ").lower()
            if choice == 'x':
                break
            else:
                continue
        include_numbers = include_numbers == 'y'

        include_symbols = input("Include symbols? (y/n): ").lower()
        if include_symbols not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            choice = input("Press 'c' to continue or 'x' to exit: ").lower()
            if choice == 'x':
                break
            else:
                continue
        include_symbols = include_symbols == 'y'

        password = generate_password(length, include_upper, include_lower, include_numbers, include_symbols)
        if password:
            print("Generated Password:", password)

if __name__ == "__main__":
    main()
