n = int(input("Enter a positive integer here: "))
lst = []
for i in range(1,n):
    x = n % i
    if x == 0:
        lst.append(i)
lst.sort()
print("Largest Prime factor of the given number is: ",lst[-1])
input("Enter any key to exit")