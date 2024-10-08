import csv
import sys

import ics
import arrow


def format_time(date: str, time: str, datetime_type):
    month, day, year = map(int, date.split('/'))
    if time:
        hour, minute = map(int, time.split(':'))
    elif datetime_type == 'start':
        hour, minute = 0, 0
    elif datetime_type == 'end':
        hour, minute = 23, 59
    else:
        raise TypeError(f"invalid datetime_type {datetime_type}")
    nyc = arrow.now("America/New_York").tzinfo
    dt = arrow.get(year, month, day, hour, minute)
    return dt.astimezone(nyc)


src = csv.reader(sys.stdin)
header = src.__next__()
events = []
for i, row in enumerate(src):
    by_key = lambda key: row[header.index(key)]
    description = ""
    description += (by_key("Category") + "\n\n") if by_key("Category") else ""
    description += by_key("Body")
    description += ("\n\n" + by_key("Link")) if by_key("Link") else ""
    e = ics.Event(
        name=by_key("Title"),
        begin=format_time(by_key("Date"), by_key("Time"), "start"),
        end=format_time(by_key("EndDate"), by_key("EndTime"), "end"),
        description=description,
    )
    events.append(e)

c = ics.Calendar(events=events)
sys.stdout.writelines(c.serialize_iter())
