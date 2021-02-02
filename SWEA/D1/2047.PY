s = input()

for i in s:
    
    if (ord(i) >= 97) and (ord(i) <= 122):
        print(chr(ord(i)-32),end="")
    else:
        print(i,end="")