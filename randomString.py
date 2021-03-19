import random 
import string
import sys

# The first argument is always the script's name, so set the second argument as
# the output length.
length = int(sys.argv[1])

random.seed()

def getRandomString(length):
    letters = string.ascii_letters
    result = ""
    for i in range(length):
        result += random.choice(letters)
    return result

randomString = getRandomString(length)
print(randomString)
