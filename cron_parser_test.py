import pytest

from cron_parser import parseCron, parseDateTimePart

@pytest.mark.parametrize(
    "inputString, outputString", 
    [(
        "5,4,3,2,1 0 10/5,15-20 * * /usr/bin/find -name test",
        [
            "minute        1 2 3 4 5",
            "hour          0",
            "day of month  10 15 16 17 18 19 20 25 30",
            "month         1 2 3 4 5 6 7 8 9 10 11 12",
            "day of week   0 1 2 3 4 5 6",
            "command       /usr/bin/find -name test"
        ]
    ),(
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


@pytest.mark.parametrize(
    "inputString, minValue, maxValue, label, errorMessage", 
    [
        ( "70", 0, 59, "minute", "minute value out of range: 70" ), 
        ( "-6", 0, 59, "minute", "minute part invalid: -6" ), 
        ( "6-", 0, 59, "minute", "minute part invalid: 6-" ), 
        ( "30-31", 0, 12, "hour", "hour value out of range: 30" ), 
        ( "12-31", 0, 12, "hour", "hour value out of range: 31" ), 
        ( "12-6", 0, 12, "hour", "hour part invalid: 12 greater than 6" ),
        ( "*/13", 0, 12, "month", "month value out of range: */13" ),
        ( "15/5", 0, 12, "month", "month value out of range: 15/5" ),
        ( "5/", 0, 12, "month", "month part invalid: 5/" ),
        ( "/5", 0, 12, "month", "month part invalid: /5" ),
    ]
)
def testInvalidValues(inputString, minValue, maxValue, label, errorMessage):
    with pytest.raises(ValueError) as e:
        parseDateTimePart(inputString, minValue, maxValue, label)
    
    assert str(e.value) == errorMessage