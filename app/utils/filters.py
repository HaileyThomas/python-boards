from datetime import datetime


def format_date(date):
    return date.strftime('%m/%d/%y')


def format_plural(amount, word):
    if amount != 1:
        return word + 's'

    return word
