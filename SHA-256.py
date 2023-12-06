import hashlib

#Takes in a password, converts the line 
# into byte form, converts the byte form to a SHA-256 hash
password = input("What is the password you want the program to crack?\n")

passSHA = hashlib.sha256(password.encode())
passSHA = passSHA.hexdigest()

crackedPassSHA = ""

#Runs through the text file with the most common passwords, converts the line 
# into byte form, converts the byte form to a SHA-256 hash, compares each line to 
# the SHA-256 password hash to try and crack it
with open('commonpasswords.txt', 'r') as f:
    for line in f:
        #strips trailing whitespaces
        line = line.strip()
        #changes line to byte format
        lineSHA = hashlib.sha256(line.encode())
        #changes the byte format to an SHA-256 hash
        lineSHA = lineSHA.hexdigest()

        #checks if the sha-256 hash line from the file equals the password hash
        if lineSHA == passSHA:
            crackedPassSHA = line

#If the program did not find the password in the text file it will return the massage 
# "password not found"
print("The password the user entered: " + password)
print ("The password as a SHA-256 hash: " + passSHA)
if crackedPassSHA == "":
    crackedPassSHA = "Password not found"

print("The password the program cracked using SHA-256 cracker: " + crackedPassSHA)