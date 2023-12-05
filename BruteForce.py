
import itertools

#Takes in a password
passwordOG = input("What is the password you want the program to crack?(Y/N)\n")
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

#Determines what character strings to add to the main string for password cracking
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
# Takes in the main string containing all possible characters and 
for c in itertools.product(strChar, repeat=len(passwordOG)):
    
    password = c
    
    print("Trying: "+ str( convertTuple(password)))
    
    if passwordOG == convertTuple(password):
        output = convertTuple(password)
        break
        

print(output)
