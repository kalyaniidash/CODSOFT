import random 
import string

def generate_password(length):
    characters =string.ascii_letters + string.digits + string.punctuation
    password =''.join(random.choice(characters) for i in range(length))
    return password
def main():
    while True:
        try:
            length =int(input("Enter the desired password length(0 to exit):"))
            if length == 0:
                print("Exiting the password generator.GoodBye!")
                break
            if length < 0:
                print("please enter apositive number.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid number")

if __name__ == "__main__":
    main()