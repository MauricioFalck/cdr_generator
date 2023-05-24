import random

from gen_dates import create_dates
from gen_phone import create_numbers

NUM_RECORDS = 50000

print("CREATING NUMBERS...")
numbers = create_numbers(NUM_RECORDS)
print("DONE")
print("CREATING VALID DATES...")
dates = create_dates(2023, 5, 10, 15, NUM_RECORDS)
print("DONE")
CDR = ""
SEPARATOR = "|"
with open("./cdr_list.csv", "w") as f:
    for i in range(0, NUM_RECORDS):
        a_number = str(numbers[i][0]["number"])
        a_country_code = str(numbers[i][0]["country_code"])
        a_area_code = str(numbers[i][0]["area_code"])
        b_number = str(numbers[i][1]["number"])
        b_country_code = str(numbers[i][1]["country_code"])
        b_area_code = str(numbers[i][1]["area_code"])
        start_date = str(dates[i]["start_date"])
        end_date = str(dates[i]["end_date"])
        duration = str(dates[i]["duration"])
        call_type = "VOICE"
        if random.random() < 0.85:
            call_result = "SUCCESS"
        else:
            call_result = "FAILURE"
        f.write(
            a_number
            + SEPARATOR
            + a_country_code
            + SEPARATOR
            + a_area_code
            + SEPARATOR
            + b_number
            + SEPARATOR
            + b_country_code
            + SEPARATOR
            + b_area_code
            + SEPARATOR
            + start_date
            + SEPARATOR
            + end_date
            + SEPARATOR
            + duration
            + SEPARATOR
            + call_type
            + SEPARATOR
            + call_result
            + "\n"
        )
