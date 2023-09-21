# Модуль проверки существования даты
from leap_year import leap_year_check

def date_ver(date):
    day, month, year = map(int, date.split('.'))
    step_1 = leap_year_check(year)

    if step_1 is True:
        if month == 2:
            if day <= 29 and day >= 1:
                return True 
            else:
                return False
        elif month in [4, 6, 9, 11]:
            if day <= 30 and day >= 1:
                return True   
            else:
                return False    
        else:
            if day <= 31 and day >= 1:
                return True
            else:
                return False
    else:
        if month == 2:
            if day <= 28 and day >= 1:
                return True
            else:
                return False
        elif month in [4, 6, 9, 11]:
            if day <= 30 and day >= 1:
                return True       
            else:
                return False
        else:
            if day <= 31 and day >= 1:
                return True
            else:
                return False