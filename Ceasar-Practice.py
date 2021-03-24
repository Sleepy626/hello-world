# x = ord(input('letter'))
# key = int(input('key'))
# print(chr(x + key))

# START:
# def ceasarCipherLetter(letter, key):
#     i = key * -1
#     if abs(key) >= 26:
#         key = key % 26
#     uniCodeNumber = ord(letter)
#     shiftUnicodeNumber = (uniCodeNumber + key) * -(i)
#     if letter.isupper() and shiftUnicodeNumber > 90:
#         shiftUnicodeNumber -= 26
#     if letter.islower() and shiftUnicodeNumber > 122: # only works from z to a
#         shiftUnicodeNumber -= 26
#     encryptedLetter = chr(shiftUnicodeNumber)
#     return encryptedLetter


# print(ceasarCipherLetter('A', -30))

# To go from a to z and z to a
# def ceasarCipherLetter(letter, key):
#     if abs(key) >= 26:
#         keyTemp = key % 26
#         if key < 0:
#             key = -keyTemp
#         else:
#             key = keyTemp
    
#     uniCodeNumber = ord(letter)
#     shiftUnicodeNumber = (uniCodeNumber + key)

#     if letter.isupper() and shiftUnicodeNumber > 90:
#         shiftUnicodeNumber -= 26
#     if letter.islower() and shiftUnicodeNumber > 122:
#         shiftUnicodeNumber -= 26

#     if letter.isupper() and shiftUnicodeNumber < 65:
#         shiftUnicodeNumber += 26
#     if letter.islower() and shiftUnicodeNumber < 97:
#         shiftUnicodeNumber += 26

#     encryptedLetter = chr(shiftUnicodeNumber)
#     return encryptedLetter

# Farids method to make it shorter
#  def ceasarCipherLetter(letter, key):
#     if abs(key) >= 26:
#         keyTemp = key % 26
#         if key < 0:
#             key = -keyTemp
#         else:
#             key = keyTemp
#     letterTemp = letter.isupper()
#     uniCodeNumber = ord(letter)
#     shiftUnicodeNumber = (uniCodeNumber + key)

#     if letterTemp and shiftUnicodeNumber > 90:
#         shiftUnicodeNumber -= 26
#     if letterTemp and shiftUnicodeNumber < 65:
#         shiftUnicodeNumber += 26
#     if letter.islower():
#         shiftUnicodeNumber += 32

#     encryptedLetter = chr(shiftUnicodeNumber)
#     return encryptedLetter

# My method to make it shorter
# def ceasarCipherLetter(letter, key):
#     if abs(key) >= 26:
#         keyTemp = key % 26
#         if key < 0:
#             key = -keyTemp
#         else:
#             key = keyTemp
    
#     uniCodeNumber = ord(letter)
#     shiftUnicodeNumber = (uniCodeNumber + key)

#     if shiftUnicodeNumber > 90 or shiftUnicodeNumber > 122:
#         shiftUnicodeNumber -= 26

#     if shiftUnicodeNumber < 65 or letter.islower() and shiftUnicodeNumber < 97:
#         shiftUnicodeNumber += 26

#     encryptedLetter = chr(shiftUnicodeNumber)
#     return encryptedLetter

# print(ceasarCipherLetter('z', 1))
