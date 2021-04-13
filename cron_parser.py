#! /usr/bin/python3

import sys

def parseCron(inputString):
    minute = [0, 15, 30, 45]
    hour = [0]
    dayOfMonth = [1, 15]
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    dayOfWeek = [1,2,3,4,5]
    command = "/usr/bin/find"

    returnString = """minute        {}
hour          {}
day of month  {}
month         {}
day of week   {}
command       {}""".format(
            " ".join([str(i) for i in minute]),
            " ".join([str(i) for i in hour]),
            " ".join([str(i) for i in dayOfMonth]),
            " ".join([str(i) for i in month]),
            " ".join([str(i) for i in dayOfWeek]),
            command
        )

    return returnString

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print()
        exit
    else:
        print(parseCron(sys.argv[1]))
