#encryption program
import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()

random.shuffle(key)
print(key)

#ENCRYPT
plain_text = input("enter the plain_text")
cryption_text = ""

for letter in plain_text :
    index = plain_text.index(letter)
    cryption_text += key[index]

print(cryption_text)
