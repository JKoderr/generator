import string
import random


def pass_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(size))

def main():
    
    pass_length = 0      

    while True: 
        try:   
            print("Hey, I can generate password. Enter password length (must be at least 5 characters):")
            pass_length = int(input())
            if pass_length > 4:
                print(f"Your new password is: {pass_gen(pass_length)}")
                break
    
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
