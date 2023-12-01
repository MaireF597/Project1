import hashlib

password = input("What is the password you want the program to crack?\n")

passSHA = hashlib.sha256(password.encode())
passSHA = passSHA.hexdigest()

crackedPassSHA = ""

with open('commonpasswords.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lineSHA = hashlib.sha256(line.encode())
        lineSHA = lineSHA.hexdigest()

        if lineSHA == passSHA:
            crackedPassSHA = line

print("The password the user entered: " + password)
print ("The password as a SHA-256 hash: " + passSHA)
if crackedPassSHA == "":
    crackedPassSHA = "Password not found"

print("The password the program cracked using SHA-256 cracker: " + crackedPassSHA)