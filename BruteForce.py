
import itertools
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

passwordOG = "alicia"

def convertTuple(tup):
    str = ""
    for item in tup:
        str = str+item
    return str

for c in itertools.product(alphabet, repeat=len(passwordOG)):
    # Add the three letters to the first half of the password.
    password = c
    # Try to extract the file.
    print("Trying: "+ str( convertTuple(password)))
    # If the file was extracted, you found the right password.
    if passwordOG == convertTuple(password):
        output = convertTuple(password)
        break
        

print(output)
