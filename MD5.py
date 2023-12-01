import hashlib

password = input("What is the password you want the program to crack?\n")
passMD5 = hashlib.md5(password.encode())
passMD5 = passMD5.hexdigest()

crackedPassMD5 = ""

with open('commonpasswords.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lineMD5 = hashlib.md5(line.encode())
        lineMD5 = lineMD5.hexdigest()

        if lineMD5 == passMD5:
            crackedPassMD5 = line

print("The password the user entered: " + password)
print ("The password as an MD5 hash: " + passMD5)
if crackedPassMD5 == "":
    crackedPassMD5 = "Password not found"

print("The password the program cracked using MD5 cracker: " + crackedPassMD5)
