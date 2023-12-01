from itertools import permutations 

password = "166452"
charListStr = "0123456789"
charList = list(charListStr)
passLength = 6
passCrackBrute = ""


passCombinations = (list(permutations(charList, passLength))) #list created and each value inside - ('1', '1') are tuples


def convertTuple(tup):
    str = ""
    for item in tup:
        str = str+item
    return str

for x in passCombinations:
    #print(x)
    str = convertTuple(x)
    if str==password:
        passCrackBrute = str
        print(passCrackBrute)
if passCrackBrute == "":
    print("password not found")






