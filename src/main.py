import random

from cdr import CDR

NUM_CDRS = 100000
YEAR = 2023
MONTH = 5
DAY = 10
PERIOD = 15

cdr = CDR(day=DAY, month=MONTH, year=YEAR, period=PERIOD, separator="|")
with open("./cdr_data.csv", "w") as f:
    for _ in range(0, NUM_CDRS):
        if random.random() < 0.85:
            f.write(cdr.create_CDR("LOCAL"))
        else:
            f.write(cdr.create_CDR("DDD"))
