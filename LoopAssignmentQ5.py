# Assignment Name: Repetition Assignment
# Question Number: 5
# 
# TODO: Create a program that takes a password
#  string from the user and encrypts the letters
#  to go up or down the alphabet using a 
# triple-number key. The amount up or down for 
# the encryption of the alphabetical characters 
# will depend on the input from the user. Input 
# for the encryption key integers will be
#  -25 ≤ key ≤ 25.

# For example, ‘CHICKEN’ with a 1, 2, -3 would 
# be C up 1 to D, H up 2 to J, I down 3 to F, 
# then C up 1 to D, K up 2 to M, E down 3 to B,
#  and N up 1 to O. Thus the encryption 
# becomes ‘DJFDMBO’.

# date and time completed: 2021-03-12 7:46

# def ceasarCipherLetter(character, key):
#     if not character.isalpha():
#         return character
#     forceLower = character.lower()
#     num = ord(forceLower) - 97 + key
#     num %= 26
#     num += 65
#     if character.islower():
#         num += 32
#     return chr(num)

# print(ceasarCipherLetter('a', 1))

# tripleNumKey = '12-3'
# # password = input('password')
position = -1
tripleNumKey = '1,25,25,'

for character in 'CHICKEN':
    if position == (len(tripleNumKey) - 1):
        position = -1
    position += 1
    if position <= (len(tripleNumKey) - 1):
        keyNum = tripleNumKey[position]
        if keyNum == '-':
            if tripleNumKey[position + 2] == ',':
                position += 1
                keyNum = tripleNumKey[position]
                keyNum = int(keyNum) * -1
            else:
                position += 2
                keyNum = tripleNumKey[position - 1] + tripleNumKey[position] 
                keyNum = int(keyNum) * -1
        position += 1
        keyNum = int(keyNum)
        forceLower = character.lower()
        num = ord(forceLower) - 97 + keyNum
        num %= 26
        num += 65
        if character.islower():
            num += 32
        print(chr(num))

# for character in 'CHICKEN':
#     if position == (len(tripleNumKey) - 1):
#         position = -1
#     position += 1
#     if position <= (len(tripleNumKey) - 1):
#         keyNum = tripleNumKey[position]
#         if keyNum == '-':
#             position += 2
#             keyNum = tripleNumKey[position - 1] + tripleNumKey[position] 
#             keyNum = int(keyNum) * -1
#         keyNum = int(keyNum)
#         forceLower = character.lower()
#         num = ord(forceLower) - 97 + keyNum
#         num %= 26
#         num += 65
#         if character.islower():
#             num += 32
#         print(chr(num))


# for keyNum in tripleNumKey:
#     keyNum = int(keyNum)
#     for character in 'CHICKEN':
#         forceLower = character.lower()
#         num = ord(forceLower) - 97 + keyNum
#         num %= 26
#         num += 65
#         if character.islower():
#             num += 32
#         print(chr(num))

# first i didn't realize we could do negatives so i came up with this 

# tripleNumKey = '12-3'
# for character in 'CHICKEN':
#     if position == 2:
#         position = -1
#     position += 1
#     if position <= 2:
#         keyNum = tripleNumKey[position]
#         if keyNum == '-':
#             keyNum = tripleNumKey[position + 1]
#             keyNum = int(keyNum) * -1
#         keyNum = int(keyNum)
#         forceLower = character.lower()
#         num = ord(forceLower) - 97 + keyNum
#         num %= 26
#         num += 65
#         if character.islower():
#             num += 32
#         print(chr(num))

# next:
# tripleNumKey = '-1-2-3'
# for character in 'CHICKEN':
#     if position == (len(tripleNumKey) - 1):
#         position = -1
#     position += 1
#     if position <= (len(tripleNumKey) - 1):
#         keyNum = tripleNumKey[position]
#         if keyNum == '-':
#             position += 1
#             keyNum = tripleNumKey[position]
#             keyNum = int(keyNum) * -1
#         keyNum = int(keyNum)
#         forceLower = character.lower()
#         num = ord(forceLower) - 97 + keyNum
#         num %= 26
#         num += 65
#         if character.islower():
#             num += 32
#         print(chr(num))

# next:
# tripleNumKey = '-19,-18,-20,'
# for character in 'CHICKEN':
#     if position == (len(tripleNumKey) - 1):
#         position = -1
#     position += 1
#     if position <= (len(tripleNumKey) - 1):
#         keyNum = tripleNumKey[position]
#         if keyNum == '-':
#             if tripleNumKey[position + 2] == ',':
#                 position += 1
#                 keyNum = tripleNumKey[position]
#                 keyNum = int(keyNum) * -1
#             else:
#                 position += 2
#                 keyNum = tripleNumKey[position - 1] + tripleNumKey[position] 
#                 keyNum = int(keyNum) * -1
#             position += 1
#         keyNum = int(keyNum)
#         forceLower = character.lower()
#         num = ord(forceLower) - 97 + keyNum
#         num %= 26
#         num += 65
#         if character.islower():
#             num += 32
#         print(chr(num))