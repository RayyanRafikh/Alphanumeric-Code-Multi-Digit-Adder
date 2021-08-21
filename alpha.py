string = input('Enter the alphanumeric code and press enter -\n')
sum = 0
i = 0
while i<=(len(string)-1):
    if string[i].isdigit():
        x = string[i]
        if (i+1) <= (len(string)-1):
            while string[i+1].isdigit():
                x += string[i+1]
                i += 1
                if (i+1) >= len(string):
                    break
                else :
                    continue
        sum += int(x)
        if i == (len(string)-1):
            break
        else :
            i += 1
            continue
    else:
        if i == (len(string)-1):
            break
        else :
            i += 1
            continue
print("The sum of the multi-digit numbers present in the alphanumeric code {} is {}".format(string, sum))        
