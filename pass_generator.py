import string
import random
import datetime


def pass_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(size))


def main():
    
    pass_length = 0
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    save_choice = "n"

    while True: 
        try:   
            print("Hey, I can generate password. Enter password length (must be at least 5 characters):")
            pass_length = int(input())
            if pass_length > 4:
                password = pass_gen(pass_length)
                print(f"Your new password is: {password}")
                break
    
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            print("Do you want to save your password? y/n")
            save_choice = input()
            if save_choice == "n":
                return
            elif save_choice == "y":
                with open("my_passwords.txt", "a") as file:
                    file.write(f"{current_time} : {password}\n")
                break
            else:
                print("Sorry, wrong answer.")
        except ValueError:
            print("Command not recognized.")

if __name__ == "__main__":
    main()
