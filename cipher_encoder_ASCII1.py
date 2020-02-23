s=input();
k=int(input())
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        y=k%26;x=ord(i)-96;
        if x+y>26:
            print(chr(y-(26-x)+96),end="")
        else:
            print(chr(x+y+96),end="")
    if ord(i)>=65 and ord(i)<=90:
        y = k % 26;x=ord(i)-64;
        if x+y>26:
            print(chr(y-(26-x)+64),end="")
        else:
            print(chr(x+y+64),end="")
print() 
