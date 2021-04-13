import pytest

from cron_parser import parseCron

@pytest.mark.parametrize(
    "inputString, outputString", 
    [(
        "0 0 10/5 * * /usr/bin/find -name test",
        [
            "minute        0",
            "hour          0",
            "day of month  10 15 20 25 30",
            "month         1 2 3 4 5 6 7 8 9 10 11 12",
            "day of week   0 1 2 3 4 5 6",
            "command       /usr/bin/find -name test"
        ]
    ),(
        "5,10,15,30-35,45 0 1,15 * 1-5 /usr/bin/find -name test",
        [
            "minute        5 10 15 30 31 32 33 34 35 45",
            "hour          0",
            "day of month  1 15",
            "month         1 2 3 4 5 6 7 8 9 10 11 12",
            "day of week   1 2 3 4 5",
            "command       /usr/bin/find -name test"
        ]
    ), (
        "* 0 1,15 * 1-5 /usr/bin/find",
        [
            "minute        {}".format(" ".join([str(i) for i in range(0,60)])),
            "hour          0",
            "day of month  1 15",
            "month         1 2 3 4 5 6 7 8 9 10 11 12",
            "day of week   1 2 3 4 5",
            "command       /usr/bin/find"
        ]
    ), (
        "5/15 0 1,15 * 1-5 /usr/bin/find",
        [
            "minute        5 20 35 50",
            "hour          0",
            "day of month  1 15",
            "month         1 2 3 4 5 6 7 8 9 10 11 12",
            "day of week   1 2 3 4 5",
            "command       /usr/bin/find"
        ]
    ), (
        "*/15 0 1,15 * 1-5 /usr/bin/find",
        [
            "minute        0 15 30 45",
            "hour          0",
            "day of month  1 15",
            "month         1 2 3 4 5 6 7 8 9 10 11 12",
            "day of week   1 2 3 4 5",
            "command       /usr/bin/find"
        ]
    )]
)
def testParseCron(inputString, outputString):
    assert parseCron(inputString) == outputString