import json
from datetime import datetime, timedelta

data = [
    {
        "shoulders": ["Standing rear delt pull", "Cable lateral raise"],
        "back": ["Cable or dumbbell row", "Pull down"],
        "hamstrings": ["Leg curl", "Heavy squat"],
    },
    {
        "shoulders": ["Standing rear delt pull", "Cable lateral raise"],
        "triceps": ["Tricept pushdown", "Dips"],
        "chest": ["Standing dumbbell press"],
    },
    {
        "mobility": ["Split squat", "Stair master"],
        "hamstrings": ["Leg curl"],
        "quads": ["Light squat", "Leg extension"],
    },
]

WEEKS = 12
start_date = datetime.now() + timedelta(days=1)
res = {}  # {date: {part: [exercises]}}
j = 0

for i in range(WEEKS * 7):
    date = start_date + timedelta(days=i)
    if date.weekday() < 6:
        res[date.strftime("%Y-%m-%d")] = data[j % len(data)]
    j += 1

print(json.dumps(res, indent=2))
