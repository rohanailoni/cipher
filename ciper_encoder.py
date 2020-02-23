****************************************************************************************************************************************
*********************************#code by rohab ailoni#time complexity O(n)*************************************************************
****************************************************************************************************************************************
s=input()                                                           #inputs the strings to be decoded
k=int(input())                                                      #ceaser constant
st="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"           #enrolls alphabets in a order
num="0123456789"                                                    #enrolls number from 0-9;    
char = "!@#$%^&*()_+-= `~,./<>?:;'{}[]|"                            #enrolls all the charecters on the stansrd keybord
for i in s:                                                         #take a alphabets or char or num from the given
    if i in st:                                                     #checks weather the i in s present in the group st so it rins n times it has time complexity of O(n)
        y = k % 52                                                  #52 represents the length of the st;    
        x=st.index(i)+1;                                            #declares x as index of a char +1
        alpha=52-x;                                                 #declares alpha
        if x+y>52:                                                  #if x+y is greater tha 52 then it means y that the y exceeing the index of st
            b=y-alpha;                                              #so b-1 is the elemnt in the st that is to change     
            print(st[b-1],end="")
        else:
            print(st[x+y-1],end="")                                 #else it means index is within the range 
    if i in num:                                                    #in ceaser cipher the number are not bee neglected so it has to changed by the cesaer constant
        y = k % 10;`                                                #the same above technique as the length of the string num is 10
        x = num.index(i) + 1                                        # so k is taken for mod 10
        alpha = 10 - x;                                             #same method as in st
        if x + y > 10:                                              
            b = y - alpha;
            print(num[b-1], end="")
        else:
            print(num[x+y-1], end="")
    if i in char:                                                   #if that is the char ie,except alpa and numerals then no change is required
        print(i,end="")
