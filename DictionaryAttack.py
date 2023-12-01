password = input("What is the password you want the program to crack?\n")
crackedPassDict = ""

with open('commonpasswords.txt', 'r') as f:
    for line in f:
        line = line.strip()
       

        if line == password:
            crackedPassDict = line
if crackedPassDict != password:
    crackedPassDict = "Password not found"
    
print("The password the user entered: " + password)
print("The password the program cracked using Dictionary Attack: " + crackedPassDict)