# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

a1, b1 = int(input("Введите числитель первой дроби: ")), int(input("Введите знаменатель первой дроби: "))
a2, b2 = int(input("Введите числитель второй дроби: ")), int(input("Введите знаменатель второй дроби: "))
a_prod = a1 * a2 
b_prod = b1 * b2
if b_prod % a_prod == 0:
    b_prod = b_prod//a_prod
    a_prod = 1
print(f"Математическое произведение дробей {a1}/{b1} * {a2}/{b2} = {a_prod}/{b_prod}")
f1 = Fraction(a1, b1)
f2 = Fraction(a2, b2)
print(f"Произведение дробей с помощью функции 'fractions': {f1 * f2}")
a_summ = a1 * b2 + a2 * b1
b_summ = b1 * b2
if b_summ % a_summ == 0:
    b_summ = b_summ//a_summ
    a_summ = 1
print(f"Математическая сумма дробей {a1}/{b1} + {a2}/{b2} = {a_summ}/{b_summ}")
print(f"Сумма дробей с помощью функции 'fractions': {f1 + f2}")

