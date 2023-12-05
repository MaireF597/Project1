

def listToString(list):
      string1 = ""
      return (string1.join(list))


def bruteForce(length):

      password = "AA"

      numArray1 = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

      passG = ""
     # while password!=passG:
      g = 0
      for index in range(len(numArray1)):
            print(index)
            print(numArray1[index])
            print(numArray1[index]+numArray1[index+g])
            g = g+1

                  

if __name__ == "__main__":
      bruteForce(2)





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









password = "abc"
str = "abcdefghijklmnopqrstuvwxyz"
strLen = len(str)
output = ""
passLength = len(password)

def loopy():
    c=1
    for strLen in str:
        output = ""
        output = output+strLen
        if c<passLength:
            c=c+1
            loopy()
        

loopy()