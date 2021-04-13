#! /usr/bin/python3

import sys

def parseDateTimePart(dateTimePart, minValue, maxValue):
    # special case, all possible minues
    if dateTimePart == "*":
        return range(minValue,maxValue+1)

    minuteList = []

    # Divide into the possible sections
    for part in dateTimePart.split(","):
        if "/" in part:
            # use a regex
            splitValues = part.split("/")
            assert len(splitValues) == 2
            if splitValues[0] == "*":
                splitValues[0] = minValue

            increment = int(splitValues[1])
            total = int(splitValues[0])
            
            while total <= maxValue:
                minuteList.append(total)
                total += increment

            
        elif "-" in part:
            splitValues = part.split("-")
            # TODO: Add validation, value 2 > value 1, values < 60 etc

            minuteList.extend(range(int(splitValues[0]), int(splitValues[1])+1))
        else:
            # TODO: Validate < 60
            minuteList.append(part)


    return minuteList

def parseCron(inputString):
    inputParts = inputString.split(" ")
    
    minute = parseDateTimePart(inputParts[0], 0, 59)
    hour = parseDateTimePart(inputParts[1], 0, 23)
    dayOfMonth = parseDateTimePart(inputParts[2], 1, 31)
    month = parseDateTimePart(inputParts[3], 1, 12)
    dayOfWeek = parseDateTimePart(inputParts[4], 0, 6)
    command = " ".join(inputParts[5:])

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
