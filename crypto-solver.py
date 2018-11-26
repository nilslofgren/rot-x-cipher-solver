# Program to ask user for plaintext input
# and x value to perform rot(x)
# return encoded input that was passed
# and work to decode the new string only using ciphertext
import nltk as nltk
from nltk.tokenize import word_tokenize
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# Read in the file and populate the translation dictionary
def read_dictionary(filename):
    dictionary = {}
    # Open dictionary file
    with open(filename, encoding='utf-8', mode='r') as myfile:
        lines = myfile.read().splitlines()
        for line in lines:
            line.lower()
            dictionary[line] = line

    return dictionary

def encrypt(str, val):
    str = str.lower()
    ciphertext = ""
    words = word_tokenize(str)
#    print(words)
    for word in words:
        for let in word:
            if let in letters:
                index = letters.index(let)
                newVal = index + val
                if newVal >= 26:
                    newVal = newVal % 26
                let = letters[newVal]
            ciphertext += let
        ciphertext += " "
    return ciphertext


def decrypt(ct):
    words = word_tokenize(ct)
    filename = "C:\\~file-path-here~\\words.txt"

    word_dict = read_dictionary(filename)
    plaintext = ""
    decrypted = False
    test_word = words[random.randint(0, len(words) - 1)]
    print(test_word)
#    print("sghr" in word_dict)
#    print(test_word in word_dict)

##    least = min(words, key=len) # returns shortest string in list
    while not decrypted:
        key = 0
##        if len(least) == 1:
##            while least != 'a' and least != 'i':
##                lIndex = letters.index(least)
##                lIndex -= 1
##
##                if lIndex < 0:
##                    lIndex += 26
##                least = letters[lIndex]
##                key += 1

        while not (plaintext in word_dict):
#            print(plaintext in word_dict)
            plaintext = ""
            for let in test_word:
                if let in letters:
                    index = letters.index(let)
                    newVal = index - key
                    if newVal < 0:
                        newVal = newVal + 26
                    let = letters[newVal]
                plaintext += let
            key += 1
#        print(plaintext in word_dict)
#        print(plaintext)
#        print(key)
        plaintext = ""
        key -= 1
        for word in words:
            for let in word:
                if let in letters:
                    index = letters.index(let)
                    newVal = index - key
                    if newVal < 0:
                        newVal = newVal + 26
                    let = letters[newVal]
                plaintext += let
            plaintext += " "

        decrypted = True




    return plaintext

userIn = input("What string would like encoded?")
rotX = int(input("With what rotation would like your input to be encrypted?"))
rotX = rotX % 26
enc = encrypt(userIn, rotX)
print("Here is your encrypted string:", enc)
dec = decrypt(enc) # Now work to decrypt the string given only the ciphertext
print("Here is your decrypted string:", dec)

    
