# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии


def employee_bonus(name_lst, salary_lst, bonus_lst):
    return {name : salary * float(bonus.strip("%")) / 100 for name, salary, bonus in zip(name_lst, salary_lst, bonus_lst)}


names = ["Иванов", "Петров", "Сидоров"]
salaries = [50000, 75000, 45000]
bonuses = ["10.25%", "11.05%", "10.50%"]

print(employee_bonus(names, salaries, bonuses))