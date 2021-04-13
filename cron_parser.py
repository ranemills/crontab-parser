#! /usr/bin/python3

import sys

def parseMinutes(minuteString):
    # special case, all possible minues
    if minuteString == "*":
        return range(0,60)

    minuteList = []

    # Divide into the possible sections
    minuteParts = minuteString.split(",")
    for part in minuteParts:
        if "/" in part:
            # use a regex
            splitValues = part.split("/")
            assert len(splitValues) == 2
            if splitValues[0] == "*":
                splitValues[0] = 0

            increment = int(splitValues[1])
            total = int(splitValues[0])
            
            while total < 60:
                minuteList.append(total)
                total += increment

            
        elif "-" in part:
            splitValues = part.split("-")
            # TODO: Add validation, value 2 > value 1, values < 60 etc

            minuteList.extend(range(int(splitValues[0]), int(splitValues[1])+1))
        else:
            minuteList.append(part)


    return minuteList

def parseCron(inputString):
    inputParts = inputString.split(" ")
    
    # Whilst developing, keep this to shortcut if any input gets a bit weird
    # When the command starts to have arguments, we'll change this
    assert len(inputParts) == 6


    minute = [0, 15, 30, 45]
    hour = [0]
    dayOfMonth = [1, 15]
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    dayOfWeek = [1,2,3,4,5]
    command = "/usr/bin/find"

    minute = parseMinutes(inputParts[0])
    # hour = parseMinutes(inputParts[1])
    # dayOfMonth = parseMinutes(inputParts[2])
    # month = parseMinutes(inputParts[3])
    # command = parseMinutes(inputParts[4])

    returnLines = [
        "minute        {}".format(" ".join([str(i) for i in minute])),
        "hour          {}".format(" ".join([str(i) for i in hour])),
        "day of month  {}".format(" ".join([str(i) for i in dayOfMonth])),
        "month         {}".format(" ".join([str(i) for i in month])),
        "day of week   {}".format(" ".join([str(i) for i in dayOfWeek])),
        "command       {}".format(command)
    ]
    
    return returnLines

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print()
        exit
    else:
        output = parseCron(sys.argv[1])
        for line in output:
            print(line)
