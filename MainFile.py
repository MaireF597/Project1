import sys
from MD5 import *
from SHA256 import *
from DictionaryAttack import *
from BruteForce import *
from BCrypt import *
from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
parser.add_argument('--choice', type=str, help='str: Choose what password cracking type you want to do: m for MD5 hash, b for BCrypt, s for SHA-256. D for Dictionary Attack, and B for Brute Force')
parser.add_argument('--password', type=str, help='str: input a password to crack')

args: Namespace = parser.parse_args() #determines what the arguments are from the terminal and convert them to the appropriate type

if args.choice == None:
    args.choice = "D"

if args.choice == "m":
    if(args.password == None):
        args.password = "d8578edf8458ce06fbc5bb76a58c5ca4"
    MD5(args.password)    
elif args.choice == "s":
    if(args.password == None):
        args.password = "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5"
    SHA256(args.password)
elif args.choice == "D":
    if(args.password == None):
        args.password = "qwerty"
    DictionaryAttack(args.password)
elif args.choice == "B":
    if(args.password == None):
        args.password = "def"
    BruteForce(args.password)
elif args.choice == "b":
    if(args.password==None):
        args.password = "$2a$12$D1035ZSwap0AEIddsJpKruxgGf4FuMzgdq2LxLEk.kF4Av25OlL7e"
    BCrypt(args.password)
