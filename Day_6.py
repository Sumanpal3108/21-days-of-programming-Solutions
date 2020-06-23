x = int(input("Enter a number: "))
s = []
while x > 0:
    i = x % 10
    s.append(i)
    x = x//10
    y = s.count(i)

    print("The frequency of {} is = {}".format(i,y))
input("Enter any key to exit")