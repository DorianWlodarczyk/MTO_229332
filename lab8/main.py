#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    if len(format_string) > 0:
        if shouldDo:
            matchcode = re.findall(r"\#\.\d+\j")
            positionJ = format_string.find("#J")
            if matchcode:
                positionhasz = format_string.find("#")
                positionOfNumber = positionhasz + 4
                NumberString = ""
                StringNumber = ""
                for i in range(positionOfNumber,len(format_string)):
                        StringNumber += format_string[i]
                StringNumberInt = int(StringNumber)
                NumberInHex = hex(StringNumberInt)
                HexNumberToString = str(NumberInHex)
                HexNumberToString= HexNumberToString.replace("a", "g")
                HexNumberToString= HexNumberToString.replace("b", "h")
                HexNumberToString= HexNumberToString.replace("c", "i")
                HexNumberToString= HexNumberToString.replace("d", "j")
                HexNumberToString= HexNumberToString.replace("e", "k")
                HexNumberToString= HexNumberToString.replace("f", "l")
                print(HexNumberToString)
                shouldDo=False
            else:
                print(format_string)
        else:
            shouldDo=True
    else:
        print("String is empty")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
