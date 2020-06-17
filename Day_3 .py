import math
m = int(input("Enter the starting number of GP Series: "))
n = int(input("Enter the number of terms for the GP Series: "))
r = int(input("Enter the common ratio of G.P. Series: "))
sum = 0
for i in range(n):
    print(m * (pow(r,i)))
    
    print(' ')
sum = m *((pow(r,n))-1/(r-1))
print(int(sum))
ch = input("Press a key to exit")