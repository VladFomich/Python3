# Модуль проверки високосного года


def leap_year_check(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False