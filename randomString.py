import random 
import string

random.seed()

def getRandomString(length):
    letters = string.ascii_letters
    result = ""
    for i in range(length):
        result += random.choice(letters)
    return result

randomString = getRandomString(12)
print(randomString)
