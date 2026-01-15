import string
import random

words = string.punctuation + string.digits + string.ascii_letters
words = list(words)
key = words.copy()

random.shuffle(key)

#encryption
print("___________Encryption Maker___________")
org = input("Enter: ")
cip = ""

for letter in org:
    index = words.index(letter)
    cip += key[index]

print(f"Original: {org}")
print(f"Encrypted: {cip}")

#decryption
print("_____________DECRYPTION_______________")
cip = input("Enter: ")
org = ""

for letter in cip:
    index = key.index(letter)
    org += words[index]

print(cip)
print(org)


# note encrypted words are at RANDOM
