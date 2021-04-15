#! /usr/bin/python3

import sys


def parseDateTimePart(dateTimePart, minValue, maxValue, label):
    # special case, all possible values
    if dateTimePart == "*":
        return range(minValue,maxValue+1)

    minuteList = []

    # Divide expression into its components
    for part in dateTimePart.split(","):
        if "/" in part:
            # Interval reccurrence
            splitValues = part.split("/")
            
            if len(splitValues) != 2 or splitValues[0] == "" or splitValues[1] == "":
                raise ValueError("{} part invalid: {}".format(label, part))

            # Interpret * as starting at the minimum value
            if splitValues[0] == "*":
                splitValues[0] = minValue

            increment = int(splitValues[1])
            total = int(splitValues[0])

            if int(increment) > maxValue or int(increment) < minValue:
                raise ValueError("{} value out of range: {}".format(label, part))
            if int(total) > maxValue or int(total) < minValue:
                raise ValueError("{} value out of range: {}".format(label, part))

            while total <= maxValue:
                minuteList.append(total)
                total += increment

        elif "-" in part:
            # Range
            splitValues = part.split("-")
            if len(splitValues) != 2 or splitValues[0] == "" or splitValues[1] == "":
                raise ValueError("{} part invalid: {}".format(label, part))

            firstValue = int(splitValues[0])
            secondValue = int(splitValues[1])
            if firstValue < minValue or firstValue > maxValue:
                raise ValueError("{} value out of range: {}".format(label, firstValue))
            if secondValue < minValue or secondValue > maxValue:
                raise ValueError("{} value out of range: {}".format(label, secondValue))
            if firstValue > secondValue:
                raise ValueError("{} part invalid: {} greater than {}".format(label, firstValue, secondValue))

            minuteList.extend(range(int(splitValues[0]), int(splitValues[1])+1))
        else:
            partInt = int(part)
            # Absolute value
            if partInt > maxValue or partInt < minValue:
                raise ValueError("{} value out of range: {}".format(label, part))
            minuteList.append(partInt)

    return sorted(list(set(minuteList)))

def parseCron(inputString):
    inputParts = inputString.split(" ")
    
    minute = parseDateTimePart(inputParts[0], 0, 59, "minute")
    hour = parseDateTimePart(inputParts[1], 0, 23, "hour")
    dayOfMonth = parseDateTimePart(inputParts[2], 1, 31, "day of month")
    month = parseDateTimePart(inputParts[3], 1, 12, "month")
    dayOfWeek = parseDateTimePart(inputParts[4], 0, 6, "day of week")
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
    if(len(sys.argv) != 2):
        print("Invalid arguments")
        exit
    else:
        try:
            output = parseCron(sys.argv[1])
            for line in output:
                print(line)
        except ValueError as e:
            print("Error: {}".format(str(e)))
            
