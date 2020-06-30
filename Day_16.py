def replace_char(str):
    n = 256
    count = [0] * n
    for i in range(len(str)):
        count[ord(str[i])] += 1
    maximum,sec_maximum = 0,0
    
    for i in range(n):
        if count[i] > count[maximum]:
            sec_maximum = maximum
            maximum = i
        elif (count[i] > count[sec_maximum]) and (count[i] != count[maximum]):
            sec_maximum = i
    
    print(chr(maximum))
    print (str.replace(chr(maximum),chr(sec_maximum)))