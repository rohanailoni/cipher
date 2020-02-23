s=input()
k=int(input())
st="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
char = "!@#$%^&*()_+-=`~,./<>?:;'{}[]|"
for i in s:
    if i in st:
        y = k % 52
        x=st.index(i)+1;
        alpha=52-x;
        if x+y>52:
            b=y-alpha;
            print(st[b-1],end="")
        else:
            print(st[x+y-1],end="")
    if i in num:
        if i in num:
            y = k % 10;
            x = num.index(i) + 1
            alpha = 10 - x;
            if x + y > 10:
                b = y - alpha;
                print(num[b-1], end="")
            else:
                print(num[x+y-1], end="")
    if i in char:
        print(i,end="")
