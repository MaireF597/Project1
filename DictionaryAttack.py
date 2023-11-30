pass = "123"

with open('commonpasswords.txt', 'r') as f:
    data = f.readline()
    if data.equals(pass)