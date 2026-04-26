import random
import string

def generate_password(length=16):
    # 1. Pool together all possible characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # 2. Randomly select characters from the pool
    password_list = [random.choice(all_characters) for _ in range(length)]
    
    # 3. Join the list into a single string
    final_password = "".join(password_list)
    
    return final_password

# Test it out!
if __name__ == "__main__":
    print("Generating a 16-character password...")
    print("Your new password is:", generate_password())