import math
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
print("The quadratic equation is: {}X2 + {}X + {} = 0".format(a,b,c))
d = b**2 - 4*a*c
print('The value of d is: ',d)
if d>0:
    
    r1 = (-b + math.sqrt(d))/(2 * a)
    r2 = (-b - math.sqrt(d))/(2 * a)
    print("Roots are real and unequal ",r1,r2)
elif d==0:
    
    r1 = -b/(2*a)
    print("Roots are real and same ",r1)
else:
    
    A = (-b/(2*a)) 
    s = (4*a*c - b**2)      
    B = (math.sqrt(s))/(2 * a)
   
    print("Roots are complex and imaginary {} + {}i  and {} - {}i".format(A,B,A,B))
    