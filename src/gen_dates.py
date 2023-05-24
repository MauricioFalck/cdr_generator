import datetime
import random


def create_dates(
    year: int, month: int, day: int, period_in_min: int, number_records: int
) -> list:
    output_dates = []
    for _ in range(0, number_records):
        output_dates.append(gen_date(year, month, day, period_in_min))
    return output_dates


def get_duration() -> int:
    duration_prob = random.random()
    if duration_prob <= 0.1:
        duration = random.randint(1, 9)
    elif duration_prob > 0.1 and duration_prob < 0.8:
        duration = random.randint(10, 30 * 60)  # 30 min
    else:
        duration = random.randint(30 * 60 + 1, 300 * 60)
    return duration


def gen_date(year: int, month: int, day: int, period_in_min: int) -> dict:
    end_date = datetime.datetime(
        year=year,
        month=month,
        day=day,
        hour=random.randint(0, 23),
        minute=random.randint(0, period_in_min - 1),
    )
    duration = get_duration()
    start_date = int(end_date.timestamp()) - duration
    return {
        "start_date": start_date,
        "end_date": int(end_date.timestamp()),
        "duration": duration,
    }
