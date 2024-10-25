import re

def is_valid_phone_number(phone_number):
    phone_regex = re.compile(r'^\+\d{1,3}\s?\d{4,14}$')
    return bool(phone_regex.match(phone_number))

def is_valid_name(name):
    name_regex =  re.compile(r"^[A-Za-z\s'-]+$")
    return bool(name_regex.match(name))