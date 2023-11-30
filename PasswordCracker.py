

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


