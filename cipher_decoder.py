s=input()
k=int(input())
st="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
char = "!@#$%^&*()_+-=`~,./<>?: ;'{}[]|"

for i in s:
    if i in st:
        y=k%52;
        x=st.index(i)+1;
        if x>y:
            print(st[x-y-1],end="")
        else:
            alpha=52-(y-x);
            print(st[alpha-1],end="")
    if i in char:
        print(i,end="")
    if i in num:
        y=k%10;
        x=num.index(i)+1;
        if x>y:
            print(num[x-y-1],end="")
        else:
            alpha=10-(y-x)
            print(num[alpha-1])

