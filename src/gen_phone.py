import random


def add_zeros(num: int, size: int) -> str:
    if num < 10**size:
        num_zeros = size - len(str(num))
        output = ""
        for i in range(0, num_zeros):
            output = output + "0"
        return output + str(num)
    else:
        return str(num)


def get_suffix(size: int) -> str:
    return add_zeros(random.randrange(0, 10**size), size)


def get_prefix(start: int, size: int) -> str:
    return str(random.randrange(start, 10**size))


def create_number_pair(
    area_size: int,
    area_list: list,
    area_src: int,
    prefix_size: int,
    prefix_start: int,
    suffix_size: int,
    country_code: int,
    call_type: str,
):
    num_a = {}
    num_b = {}

    num_a["number"] = get_prefix(prefix_start, prefix_size) + get_suffix(suffix_size)
    num_b["number"] = get_prefix(prefix_start, prefix_size) + get_suffix(suffix_size)

    if call_type == "LOCAL":
        num_a["area_code"] = add_zeros(area_src, area_size)
        num_b["area_code"] = add_zeros(area_src, area_size)
    if call_type == "DDD":
        area_list.pop(area_list.index(area_src))
        rand_area = area_list[random.randrange(0, len(area_list))]
        if random.random() < 0.5:
            num_a["area_code"] = add_zeros(area_src, area_size)
            num_b["area_code"] = add_zeros(rand_area, area_size)
        else:
            num_b["area_code"] = add_zeros(area_src, area_size)
            num_a["area_code"] = add_zeros(rand_area, area_size)
    num_a["country_code"] = country_code
    num_b["country_code"] = country_code

    return (num_a, num_b)
