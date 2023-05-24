import random

from cdr import CDR

NUM_CDRS = 500000
YEAR = 2023
MONTH = 5
DAY = 10
PERIOD = 15
SEPARATOR = "|"

cdr = CDR(day=DAY, month=MONTH, year=YEAR, period=PERIOD, separator=SEPARATOR)
with open("./cdr_data.csv", "w") as f:
    for _ in range(0, NUM_CDRS):
        if random.random() < 0.75:
            if random.random() < 0.2:
                f.write(cdr.create_CDR("SMS", "LOCAL"))
            else:
                f.write(cdr.create_CDR("VOICE", "LOCAL"))
        else:
            if random.random() < 0.2:
                f.write(cdr.create_CDR("SMS", "DDD"))
            else:
                f.write(cdr.create_CDR("VOICE", "DDD"))
