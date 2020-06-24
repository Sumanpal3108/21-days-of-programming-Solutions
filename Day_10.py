s = list(input("Enter a list of numbers here: "))
temp = s[0]
s[0] = s[-1] 
s[-1] = temp
print(s)
input("Enter any key to exit")