import hashlib

password = input("What is the password you want the program to crack?\n")
PassMD5 = hashlib.md5(password.encode())
print(PassMD5)



