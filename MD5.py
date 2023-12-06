import hashlib

#Takes in a password, converts the line 
# into byte form, converts the byte form to an MD5 hash
password = input("What is the password you want the program to crack?\n")
passMD5 = hashlib.md5(password.encode())
passMD5 = passMD5.hexdigest()

crackedPassMD5 = ""

#Runs through the text file with the most common passwords, converts the line 
# into byte form, converts the byte form to an MD5 hash, compares each line to 
# the MD5 password hash to try and crack it
with open('commonpasswords.txt', 'r') as f:
    for line in f:
        #strips trailing whitespaces
        line = line.strip()
        #changes line to byte format
        lineMD5 = hashlib.md5(line.encode())
        #changes the byte format to an MD5 hash
        lineMD5 = lineMD5.hexdigest()

        #checks if the MD5 hash line from the file equals the password hash
        if lineMD5 == passMD5:
            crackedPassMD5 = line

#If the program did not find the password in the text file it will return the massage 
# "password not found"
print("The password the user entered: " + password)
print ("The password as an MD5 hash: " + passMD5)
if crackedPassMD5 == "":
    crackedPassMD5 = "Password not found"

print("The password the program cracked using MD5 cracker: " + crackedPassMD5)
