import uuid
import re
import math


def create_uuid():
    return str(uuid.uuid4())


def alpha_numeric(receipt_name: str):
    no_spaces = receipt_name.replace(" ", "")
    only_alpha_numeric = re.sub(r'[^\w\s]', '', no_spaces)
    return len(only_alpha_numeric)


def round_dollar(amount: str):
    float_amount = float(amount)
    return 50 if float_amount.is_integer() else 0


def multiple_quarter(amount: str):
    float_amount = float(amount)
    return 25 if float_amount % 0.25 == 0 else 0


def items_even(list_length: int):
    divided_by_two = list_length / 2
    rounded_down = math.floor(divided_by_two)
    return rounded_down * 5


def description_length(description: str, price: float):
    trimmed_description = description.strip()
    if len(trimmed_description) % 3 == 0:
        times_two = price * 0.2
        return math.ceil(times_two)
    return 0


def date_odd(date: str):
    split_date = date.split("-")
    day = int(split_date[-1])
    return 6 if day % 2 != 0 else 0


def purchase_time(time: str):
    split_date = time.split(":")
    hour = int(split_date[0])
    minutes = int(split_date[1])

    if hour < 14 or hour > 15:
        return 0
    elif hour == 15:
        return 10
    elif hour == 14 and minutes == 0:
        return 0
    else:
        return 10
