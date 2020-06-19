b = input("Input a binary number: ")
x = b.split()
b_string = ""
for x in x:
    i = int(x,2)
    b_character = chr(i)
    
    b_string += b_character
    
print(b_string)
ch = input("Enter any key to exit")