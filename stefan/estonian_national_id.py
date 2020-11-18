import datetime
from typing import Union

SEX_FEMALE = 'F'
SEX_MALE = 'M'


def get_sex(personal_code: str) -> Union[SEX_FEMALE, SEX_MALE]:
    if personal_code[0] in ['1', '3', '5', '7']:
        return SEX_MALE
    elif personal_code[0] in ['2', '4', '6', '8']:
        return SEX_FEMALE


def calculate_birth_year(personal_code: str) -> int:
    if personal_code[0] in ['1', '2']:
        year_digits = '18'
    elif personal_code[0] in ['3', '4']:
        year_digits = '19'
    else:
        year_digits = '20'

    return int(f'{year_digits}{personal_code[1:3]}')


def convert_to_birthdate(personal_code: str) -> datetime.date:
    birth_year = calculate_birth_year(personal_code)
    birth_month = int(personal_code[3:5])
    birth_day = int(personal_code[5:7])

    return datetime.date(year=birth_year, month=birth_month, day=birth_day)
