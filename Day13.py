n = int(input("Enter a positive integer here: "))
lst1 = 0
lst2 = []
for i in range(2,n+1):
    if n % i == 0:
        for j in range(2,int(i/2)):
            if i % j == 0:
                lst1 = 1
                break
        if lst1 == 0:
            
            print(i)  
            lst2.append(i)
print("Largest Prime factor of the given number is: ",lst2[-1])
input("Enter any key to exit")