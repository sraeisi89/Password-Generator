
# Write a password generator in Python. Be creative with how you
# generate passwords - strong passwords have
# a mix of lowercase letters, uppercase letters, numbers, and
# symbols. The passwords should be random, generating a new
# password every time the user asks for a new password.
# Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import string
import random

## characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## length of password from the user
    length = int(input("Enter password length: "))

    ## shuffling the characters
    random.shuffle(characters)

    ## picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    print("".join(password))


## invoking the function
generate_random_password()
