import random

from gen_dates import gen_date
from gen_phone import create_number_pair


class CDR:
    def __init__(self, year, month, day, period, separator) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.period = period
        self.separator = separator

    def create_CDR(self, call_type, call_dist):
        cdr_date = gen_date(self.year, self.month, self.day, self.period)

        area_list = [11, 21, 31, 12, 81, 61, 41]

        if call_dist == "LOCAL":
            num_a, num_b = create_number_pair(
                area_size=2,
                area_list=area_list,
                area_src=11,
                prefix_size=4,
                prefix_start=4000,
                suffix_size=4,
                country_code=55,
                call_type="LOCAL",
            )
        if call_dist == "DDD":
            num_a, num_b = create_number_pair(
                area_size=2,
                area_list=area_list,
                area_src=11,
                prefix_size=4,
                prefix_start=4000,
                suffix_size=4,
                country_code=55,
                call_type="DDD",
            )

        if call_type == "SMS":
            cdr_date["duration"] = 0
            cdr_date["end_date"] = cdr_date["start_date"]

        a_number = str(num_a["number"])
        a_country_code = str(num_a["country_code"])
        a_area_code = str(num_a["area_code"])
        b_number = str(num_b["number"])
        b_country_code = str(num_b["country_code"])
        b_area_code = str(num_b["area_code"])
        start_date = str(cdr_date["start_date"])
        end_date = str(cdr_date["end_date"])
        duration = str(cdr_date["duration"])
        if random.random() < 0.85:
            call_result = "SUCCESS"
        else:
            call_result = "FAILURE"

        return (
            a_number
            + self.separator
            + a_country_code
            + self.separator
            + a_area_code
            + self.separator
            + b_number
            + self.separator
            + b_country_code
            + self.separator
            + b_area_code
            + self.separator
            + start_date
            + self.separator
            + end_date
            + self.separator
            + duration
            + self.separator
            + call_type
            + self.separator
            + call_result
            + " \n"
        )
