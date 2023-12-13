import bcrypt

def BCrypt(password):
    crackedPassBcrypt = ""
    #print(password)
    #converts password into byte format
    passwordByte = password.encode('utf-8') 
    #print(passwordByte)

    #runs through list of most common passwords and encodes the line in byte format then 
    # compares the password input with the password from the line of the file
    with open('commonpasswords.txt', 'r') as f:
            for line in f:
                #strips trailing whitespaces
                line = line.strip()

                #encodes line in byte format
                lineByte = line.encode('utf-8')
                
                #checks to see if the input password is equal to the password in the 
                # file by using the same salt value to encode it (takes the input password 
                # in byte format and seperates the salt from the hash and puts the line in byte 
                # format with the salt then hashes it to check if the entered password is equal to the line)
                value = bcrypt.checkpw(lineByte, passwordByte)
                if (value):
                    #print(lineByte)
                    crackedPassBcrypt = line
                    break

    print("The password the user entered: " + password)
    
    #If the program did not find the password in the text file it will return an error message
    if crackedPassBcrypt == "":
        crackedPassBcrypt = "Password not found"

    print("The password the program cracked using BCrypt cracker: " + crackedPassBcrypt)

#BCrypt("$2a$12$D1035ZSwap0AEIddsJpKruxgGf4FuMzgdq2LxLEk.kF4Av25OlL7e")