n = int(input("Enter the number of scores: "))
A = []
for i in range(1,n+1):
    A.append(i)
A.sort()
print(A)
print("The runner-up score is: ",A[n-2])
input("Enter any key to exit")    