from . import jalali
from django.utils import timezone


def converter_number_to_persian(mystr):
    num = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }


def jalali_converter(time):
    time = timezone.localtime(time)
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    jmonth = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    output_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    output_to_string = jalali.Gregorian(time_to_str).persian_string()

    time_to_list = list(output_to_tuple)
    output_to_nmonth_saat = "{}/{}/{}، ساعت {}:{}".format(
        time_to_list[0], time_to_list[1], time_to_list[2], time.hour, time.minute
    )

    return output_to_nmonth_saat
