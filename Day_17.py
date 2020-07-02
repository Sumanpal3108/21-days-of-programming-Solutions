def fibonacci(a,b,n):
    if n>0:
        print (a+b)
        fibonacci(b,a+b,n-1)
        
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
n=int(input("Enter the no of terms you want to dispaly: "))
print("Fibonacci Series")
print (a)
print (b)
fibonacci(a,b,n-2)
h=input("Enter any key")