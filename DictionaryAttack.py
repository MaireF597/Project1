#Takes in a password
password = input("What is the password you want the program to crack?\n")
crackedPassDict = ""

#Runs through the text file with the most common passwords and compares each line to 
# the password input to try and crack it
with open('commonpasswords.txt', 'r') as f:
    for line in f:
        #strips trailing whitespaces
        line = line.strip()
       
        #checks if the line from the file equals the password
        if line == password:
            crackedPassDict = line
#If the program did not find the password in the text file it will return the massage 
# "password not found"
if crackedPassDict != password:
    crackedPassDict = "Password not found"
    
print("The password the user entered: " + password)
print("The password the program cracked using Dictionary Attack: " + crackedPassDict)