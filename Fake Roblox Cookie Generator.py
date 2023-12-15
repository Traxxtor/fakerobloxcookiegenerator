import random
import string

def display_menu():
    print("1. Bake a working Roblox cookie!")
    print("2. Exit")

def generate_random_password(length=1581):
    # Exclude special characters from the characters string
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        display_menu()
        user_input = input("Enter your choice (1-2): ")

        if user_input == "2":
            print("Exiting the program.")
            break
        elif user_input == "1":
            print(".Your cookie is baked!")
            password = generate_random_password()
            print(f".ROBLOSECURITY=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_{password}\n")
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
