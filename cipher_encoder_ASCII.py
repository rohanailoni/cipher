s=input();
k=int(input())
for i in s:
    elif ord(i)>=97 and ord(i)<=122:
        y=k%26;x=ord(i)-96;
        if x+y>26:
            print(chr(y-(26-x)+96),end="")
        else:
            print(chr(x+y+96),end="")
    elif ord(i)>=65 and ord(i)<=90:
        y = k % 26;x=ord(i)-64;
        if x+y>26:
            print(chr(y-(26-x)+64),end="")
        else:
            print(chr(x+y+64),end="")
    elif ord(i)>=48 and ord(i)<=57:
        y=k%10;x=ord(i)-47;
        if x+y>10:
            print(chr(y-(10-x)+47),end="")
        else:
            print(chr(x+y+47),end="")
    else:
        print(i,end="")
