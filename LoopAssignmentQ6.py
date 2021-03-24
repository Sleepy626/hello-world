# Assignment Name: Repetition Assignment
# Question Number: 5
# 
# TODO: Create a program that takes a password string 
# from the user and encrypts the letters to go up or down 
# the alphabet using a triple-number key. The amount up or
# down for the encryption of the alphabetical characters 
# will depend on the input from the user. Input for the 
# encryption key integers will be -25 ≤ key ≤ 25.

# date and time completed: 2021-03-23 9:42

def passCheck():
    '''While True, asks the user for a password to be
encrypted. The check() function then uses a while loop
to see if the user even inputted a password. If not, 
continues looping until a password is inputted.'''
    password = input('Input a password: ')
    while True:
        if password == '':
            print('Please input a password to be encrypted')
            password = input('Input a password: ')
        else:
            return password

# The passwordChecked variable is the same as password variable,
# but checked with check() function
passwordChecked = passCheck()

def check(prompt):
    '''While True, asks the user for a key number that
will encrypt a given passowrd. The check() function
then uses the try block to see if the input is valid, 
meaning no ValueError occuring and key >= -25 and key <= 25.
If not, continues looping until a valid value is inputted.
The prompt parameter takes in an a string as an argument to
be inputted into the string below'''
    while True:
        key = input(f'Input your {prompt} encryption key\
(must be between -25 to 25): ')
        try:
            key = int(key)
            if not -25 <= key <= 25:
                raise ValueError
        except ValueError:
            print('Please put a valid number')
        else:
            return int(key)

# The three key variables below are the first three encryption keys
# checked by the check() function
key1 = check('first ')
key2 = check('second')
key3 = check('third')

# Used to count the numebr of iterations in the loop below, thus 
# determining which character of the password is being encrypted
# by which key
counter = 0

def encryption(key):
    '''Encrypts the given character with the given key'''
    lowerCharacter = character.lower()
    num = ord(lowerCharacter) - 97 + key
    num %= 26
    num += 65
    if character.islower():
        num += 32
    print(chr(num), end = '')

# Prints the header for the loop below
print('The encrypted password is: ', end = '')

# Encrypts the given password, with the given keys and prints
# the encrypted password
for character in passwordChecked:
    counter += 1
    if not character.isalpha():
        print(character, end = '')
    elif counter % 3 == 1:
        encryption(key1)
    elif counter % 3 == 2:
        encryption(key2)
    elif counter % 3 == 0:
        encryption(key3)
print('')