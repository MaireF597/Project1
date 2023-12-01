from itertools import combinations_with_replacement

password = "12"
charList = "12"
passLength = 2

passCombinations = (list(combinations_with_replacement(charList, passLength)))

print(passCombinations[0])

combLen = len(passCombinations)
count = 0
#while (count < combLen):


