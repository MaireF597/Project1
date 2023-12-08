import bcrypt

def BCrypt(password):
    crackedPassBcrypt = ""
    passwordByte = password.encode('utf-8') #converts password into byte format
    print(passwordByte)


    with open('commonpasswords.txt', 'r') as f:
            for line in f:
                #strips trailing whitespaces
                line = line.strip()

                lineByte = line.encode('utf-8')
                
                value = bcrypt.checkpw(lineByte, passwordByte)
                if (value):
                    crackedPassBcrypt = line
                    break

    print("The password the user entered: " + password)
    
    if crackedPassBcrypt == "":
        crackedPassBcrypt = "Password not found"

    print("The password the program cracked using BCrypt cracker: " + crackedPassBcrypt)

#BCrypt("$2a$12$D1035ZSwap0AEIddsJpKruxgGf4FuMzgdq2LxLEk.kF4Av25OlL7e")