import sys
from MD5 import *
from SHA256 import *
from DictionaryAttack import *
from BruteForce import *
from BCrypt import *
from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
parser.add_argument('--choice', type=str, help='str: Choose what password cracking type you want to do: m for MD5  hash, b for BCrypt, s for SHA-256. D for Dictionary, and B for Brute Force')
parser.add_argument('--password', type=str, help='str: input a password to crack')

args: Namespace = parser.parse_args() #determines what the arguments are from the terminal and convert them to the appropriate type

if args.choice == "m":
    MD5(args.password)    
elif args.choice == "s":
    SHA256(args.password)
elif args.choice == "D":
    DictionaryAttack(args.password)
elif args.choice == "B":
    BruteForce(args.password)
elif args.choice == "b":
    BCrypt(args.password)