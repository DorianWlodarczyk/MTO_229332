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
                StartOfNumber = idx+2
                newDigit = ''
                for j in range(idx+2, len(format_string)):
                    if format_string[j] >= '0' and format_string[j] <='9':
                        for k in range(len(format_string)-StartOfNumber):
                            format_string[j] = newDigit
                            newDigit = NumberString.append(k)
                    else:
                        j=j+1
                NumberStringFromArrayToString = ' '.join(NumberString)
                NumberStringIntiInt = int(NumberStringFromArrayToString)
                NumberInHex = hex(NumberStringIntiInt)
                HexNumberToString = str(NumberInHex)
                for l in range(len(HexNumberToString)):
                    if HexNumberToString[l] == 'a':
                        HexNumberToString[l] == 'g'
                        print(HexNumberToString[l])
                    if HexNumberToString[l] == 'b':
                        HexNumberToString[l] == 'h'
                        print(HexNumberToString[l])
                    if HexNumberToString[l] == 'c':
                        HexNumberToString[l] == 'i'
                        print(HexNumberToString[l])
                    if HexNumberToString[l] == 'd':
                        HexNumberToString[l] == 'j'
                        print(HexNumberToString[l])
                    if HexNumberToString[l] == 'e':
                        HexNumberToString[l] == 'k'
                        print(HexNumberToString[l])
                    if HexNumberToString[l] == 'f':
                        HexNumberToString[l] == 'l'
                        print(HexNumberToString[l])
                    else:
                        print(HexNumberToString[l])

                print(HexNumberToString[l])
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
