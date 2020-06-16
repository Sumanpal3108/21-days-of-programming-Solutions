n = int(input("Enter number of rows: "))
for i in range(n):
    print(' '*(2*(n-1-i)),end=' ')
    r = (2*i)+1
    for j in range(r):
        if (j <= (int(r/2))):
            print(chr(65+j),end=' ')
            m = (65+j)
        else:
            print((chr(m - 1 - j + (int(r/2)+1))),end=' ')
    print()
ch = input("Press a key to exit")