# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. 

from sys import argv
from date_verify import date_ver 

date = argv[1]
# date = "32.13.1975" #хардкод

print(date_ver(date))