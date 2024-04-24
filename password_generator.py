import random
import string

# Function to generate a random password
def generate_password(length=12):
    # Define characters to use in the password (letters, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password by randomly choosing characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        # Ask the user to input the length of the password they want to generate
        while True:
            try:
                password_length = int(input("Enter the length of the password you want to generate: "))
                if password_length <= 0:
                    raise ValueError("Password length should be positive.")
                break  # Exit the loop if input is valid
            except ValueError:
                print("Error: Please enter a valid positive number for the password length.")

        # Generate the password using the specified length
        generated_password = generate_password(password_length)
        # Display the generated password
        print("Generated Password:", generated_password)

        # Ask the user if they want to create another password
        create_another = input("Do you want to create another password? (yes/no): ")
        if create_another.lower() != 'yes':
            print("Thank you for using the password generator!")
            break  # Exit the loop and end the program