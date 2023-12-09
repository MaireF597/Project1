import hashlib
def MD5(password):
   
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
            #changes the byte format to an MD5 hash (hexadecimal string)
            lineMD5 = lineMD5.hexdigest()

            #checks if the MD5 hash line from the file equals the password hash
            if lineMD5 == password:
               crackedPassMD5 = line

    #If the program did not find the password in the text file it will return the massage 
    # "password not found"
    print("The password the user entered: " + password)

    if crackedPassMD5 == "":
        crackedPassMD5 = "Password not found"

    print("The password the program cracked using MD5 cracker: " + crackedPassMD5)

#MD5("d8578edf8458ce06fbc5bb76a58c5ca4")