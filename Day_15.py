str2 = input("Give your message here: ")
s = 0
for i in str2:
    if i == " ":
        print (chr(ord(i)),end = "" )
 
    elif s%2 == 0:
        print (chr(ord(i)-1),end = "" )
        s+=1
    elif s%2 == 1:
        print (chr(ord(i)+1),end = "" )
        s+=1
input("Enter any key to exit")