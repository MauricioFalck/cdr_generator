import random


def format_suffix(num: int) -> str:
    if num < 1000:
        num_zeros = 4 - len(str(num))
        output = ""
        for i in range(0, num_zeros):
            output = output + "0"
        return output + str(num)
    else:
        return str(num)


def create_numbers(total_records: int) -> list:
    avail_number = []
    total_numbers = int(total_records * 1.4)

    for _ in range(0, total_numbers):
        while True:
            num = gen_phone_number()
            if not num in avail_number:
                avail_number.append(num)
                break

    output_list = []
    for _ in range(0, total_records):
        a_num = avail_number[random.randrange(0, len(avail_number))]
        b_num = 0
        while True:
            b_num = avail_number[random.randrange(0, len(avail_number))]
            if (
                a_num["number"] != b_num["number"]
                or a_num["area_code"] != b_num["area_code"]
            ):
                break

        output_list.append((a_num, b_num))
    return output_list


def gen_phone_number() -> dict:
    country_code = "55"
    # TODO: Add different area codes
    area_code = [11, 21, 12, 31, 41, 61]
    # Prioritize traffic from area code 11 and 21
    rand = random.random()
    if rand < 0.3:
        rand_code = area_code[0]
    elif rand >= 0.3 and rand < 0.6:
        rand_code = area_code[1]
    else:
        rand_code = area_code[random.randint(2, len(area_code) - 1)]

    return {
        "country_code": country_code,
        "area_code": str(rand_code),
        "number": str(random.randrange(4000, 10000))
        + format_suffix(random.randrange(0, 10000)),
    }
