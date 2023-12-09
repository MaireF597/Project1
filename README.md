# PasswordCrackerProject

2023 CSHS Cybersecurity 


## Command Line Arguments

To choose a password cracking type to run:\
 --choice *the letter representing your choice* --password *password you want to crack* (The password and choice portion are optional as the program will set a default password and password cracking mode if the user does not input arguments)


m = MD5 Hash\
b = BCrypt\
s = SHA-256 Hash\
D = Dictionary Attack\
B = Brute Force



## Formatting
VSCode Terminal:

--choice m --password d8578edf8458ce06fbc5bb76a58c5ca4\
--choice s --password 65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5\
--choice D --password qwerty\
--choice B --password qwerty\
--choice b --password $2a$12$D1035ZSwap0AEIddsJpKruxgGf4FuMzgdq2LxLEk.kF4Av25OlL7e



Computer Terminal

Python3 MainFile.py --choice m --password d8578edf8458ce06fbc5bb76a58c5ca4\
Python3 MainFile.py --choice s --password 65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5\
Python3 MainFile.py --choice D --password qwerty\
Python3 MainFile.py --choice B --password qwerty\
Python3 MainFile.py --choice b --password $2a$12$D1035ZSwap0AEIddsJpKruxgGf4FuMzgdq2LxLEk.kF4Av25OlL7e 

## Dependencies

CyberStart America code was used in the BruteForce program 

W3schools was used in the rest of the programs 



Imports:\
sys\
itertools\
hashlib\
bcrypt


