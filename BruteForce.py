
import itertools

def BruteForce(password):
    output = ""
    print("Your password is: "+password)
    #Asks the user if their password has special characters, numbers, uppercase, lowercase to cut down on cracking time. 
    #Depending on user response, the characters are added to the main string to be used while cracking the password.
    choiceS = input("Does the password contain special characters?(Y/N)\n")
    choiceN= input("Does the password contain numbers?(Y/N)\n")
    choiceL= input("Does the password contain lowercase letters?(Y/N)\n")
    choiceU= input("Does the password contain uppercase letters?(Y/N)\n")
    alphabetLower = "abcdefghijklmnopqrstuvwxyz"
    alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "1234567890"
    special = "`~!@#$%^&*()_-+={[}]|\:;<,>.?/"

    #Determines what character strings to add to the main string (strChar) for password cracking
    strChar=" "
    if choiceS == "Y":
        strChar = strChar+special
    if choiceL == "Y":
        strChar = strChar+alphabetLower
    if choiceU == "Y":
        strChar = strChar+alphabetUpper
    if choiceN == "Y":
        strChar = strChar+number


    #Converts a tuple to string 
    def convertTuple(tup):
        str = ""
        for item in tup:
            str = str+item
        return str

    #Runs through all permutations of the characters in the main strings to crack the password
    for c in itertools.product(strChar, repeat=len(password)):
        #Makes the password we are checking against the real password equal to c which contains
        # the current permutation of str
        password = c
        
        print("Trying: "+ str( convertTuple(password)))
        
        #Checks to see if the password equals the real password and if it is, it's converted 
        # into a String to be output
        if password == convertTuple(password):
            output = convertTuple(password)
            break
            
    #If the program did not find the password in the text file it will return an error message
    if (output == ""):
        output = "Unable to crack password"
    
    print(output)
