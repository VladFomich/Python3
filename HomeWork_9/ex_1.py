# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import math
import csv
import json
import random


# Функция для нахождения корней квадратного уравнения
def quadratic_equation(a, b, c):

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:

        x1 = (-b + math.sqrt(discriminant)) / (2 * a)

        x2 = (-b - math.sqrt(discriminant)) / (2 * a)

        return x1, x2

    elif discriminant == 0:

        x = -b / (2 * a)

        return x

    else:

        return None


# Функция для генерации csv файла
def generate_csv_file(filename, num_of_rows):    

    with open(filename, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        for _ in range(num_of_rows):

            row = [random.randint(1, 1000) for _ in range(3)]

            writer.writerow(row)


# Декоратор для функции нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла
def quadratic_equation_decorator(func):

    def wrapper(filename):

        with open(filename, 'r') as csvfile:

            reader = csv.reader(csvfile)

            for row in reader:

                a, b, c = map(int, row)

                result = func(a, b, c)

                print(f"Уравнение: {a}x^2 + {b}x + {c} = 0")

                print(f"Корни: {result}")

    return wrapper


# Декоратор для сохранения переданных параметров и результатов работы функции в json файл
def quadratic_equation_results_decorator(func):

    def wrapper(*args):

        params = [str(arg) for arg in args]

        result = func(*args)

        data = {

            "params": params,

            "result": result

        }

        with open("results.json", 'a') as jsonfile:

            json.dump(data, jsonfile)
            
            jsonfile.write('\n')

    return wrapper


@quadratic_equation_decorator
@quadratic_equation_results_decorator
def quadratic_equation(a, b, c):

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:

        x1 = (-b + math.sqrt(discriminant)) / (2 * a)

        x2 = (-b - math.sqrt(discriminant)) / (2 * a)

        return x1, x2

    elif discriminant == 0:

        x = -b / (2 * a)

        return x

    else:

        return None


generate_csv_file("numbers.csv", 100)


quadratic_equation("numbers.csv")
