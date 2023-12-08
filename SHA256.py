import hashlib
def SHA256(password):

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
            if lineSHA == password:
                crackedPassSHA = line

    #If the program did not find the password in the text file it will return the massage 
    # "password not found"
    print("The password the user entered: " + password)
 
    if crackedPassSHA == "":
        crackedPassSHA = "Password not found"

    print("The password the program cracked using SHA-256 cracker: " + crackedPassSHA)

#SHA256("65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5")