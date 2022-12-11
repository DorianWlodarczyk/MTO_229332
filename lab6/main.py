#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.' and (format_string[idx+2] == 'X' or format_string[idx+2] == 'x') and (format_string[idx+3] == 'g' or format_string[idx+3] == 'G'):
                for j in range(0,len(format_string)):
                    if format_string[j] >= '0' and format_string[j] <= '9':
                        oldNumber = format_string[j]
                        oldNumberToInt = int(oldNumber)
                        newNumber = ((oldNumberToInt*9+1)%10)
                        newNumberToString = str(newNumber)
                        print(newNumber,end="")
                    else:
                        print(format_string[j], end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print(" ")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
