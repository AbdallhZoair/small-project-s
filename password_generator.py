import string
import random
 
user_pass = ""
 
try:
    length_pass = int(input("What is the length of your password? : "))
    number_of_letters = int(input("How many letters do you want? : "))
    number_of_digits = int(input("How many digits do you want? : "))
    number_of_symbols = int(input("How many symbols do you want? : "))
except ValueError:
    print("Please enter numbers only. Run the program again.")
    exit()
 
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
 
total = number_of_letters + number_of_digits + number_of_symbols
 
if length_pass == total:
    user_pass = (
        random.choices(letters, k=number_of_letters)
        + random.choices(digits, k=number_of_digits)
        + random.choices(symbols, k=number_of_symbols)
    )
    random.shuffle(user_pass)
    user_pass = "".join(user_pass)
    print(f"\nYour password is: {user_pass}")
else:
    print(f"\nError: you entered length={length_pass}, but letters + digits + symbols = {total}. They must match, try again.")
 
