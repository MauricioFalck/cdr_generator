import datetime
import random


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
        hour=15,
        minute=random.randint(30 - period_in_min, 30),
    )
    duration = get_duration()
    start_date = int(end_date.timestamp()) - duration
    return {
        "start_date": start_date,
        "end_date": int(end_date.timestamp()),
        "duration": duration,
    }
