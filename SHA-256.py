import hashlib

password = "123456"

passSHA = hashlib.sha256(password.encode())
passSHA = passSHA.hexdigest()
print(passSHA)