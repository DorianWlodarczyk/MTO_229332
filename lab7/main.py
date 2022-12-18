#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and (format_string[idx+1] == 'j' or format_string[idx+1] == 'J'):
                print_flag = True
                NumberString = []
                for j in range(idx+2, len(format_string)):
                    if format_string[j] >= '0' and format_string[j] <='9':
                        for k in range(len(format_string-(idx+2))):
                            format_string[j] = NumberString.append(k)
                    else:
                        j=j+1
                NumberStringFromArrayToString = ' '.join(NumberString)
                NumberStringIntiInt = int(NumberStringFromArrayToString)
                print(param,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
