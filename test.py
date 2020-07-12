from rfc3339 import RFC3339
from datetime import datetime, timedelta, timezone

UTC = timezone(timedelta(hours=0, minutes=0))
PST = timezone(-1 * timedelta(hours=8, minutes=0))
IND = timezone(timedelta(hours=5, minutes=30))
AMS = timezone(timedelta(hours=0, minutes=20)) 

testcases = [
    ("1985-04-12T23:20:50.52Z", datetime(1985, 4, 12, 23, 20, 50, 520000, tzinfo=UTC)),
    ("1985-04-12t23:20:50.52z", datetime(1985, 4, 12, 23, 20, 50, 520000, tzinfo=UTC)),
    ("1996-12-19T16:39:57-08:00", datetime(1996, 12 ,19, 16, 39, 57, 000000, tzinfo=PST)),
    ("1996-12-19T16:39:57+05:30", datetime(1996, 12 ,19, 16, 39, 57, 000000, tzinfo=IND)),
    ("1990-12-31T23:59:60Z", datetime(1990, 12, 31, 23, 59, 59, tzinfo=UTC)),  # avoid leap seconds.
    ("1990-12-31T15:59:60-08:00", datetime(1990, 12, 31, 15, 59, 59, tzinfo=PST)),
    ("1937-01-01T12:00:27.87+00:20", datetime(1937, 1, 1, 12, 0, 27, 870000, tzinfo=AMS)),
]

for testcase in testcases:
    validator = RFC3339()
    got, want = validator.extract_datetime(testcase[0]), testcase[1]
    if got != want:
        assert(got == want)  # To raise an appropriate exception.
    else:
        print("{} passed.".format(validator.encode_datetime(got)))

