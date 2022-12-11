#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.' and (format_string[idx+2] == 'X' or format_string[idx+2] == 'x') and (format_string[idx+3] == 'g' or format_string[idx+3] == 'G'):
                for j in range(0,len(format_string)):
                    oldNumber = format_string[j]
                    newNumber = ((oldNumber*9+1)%10)
                print(newNumber,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

